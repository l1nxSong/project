from flask import Flask, render_template, request, redirect, render_template_string, flash
from decimal import Decimal
from markupsafe import escape
import settings
import json
import pymongo
import hashlib
import logging
import time
from test import Test

app = Flask(__name__)
app.config.from_object(settings)
app.secret_key = 'somethingSecret'

currentUser = {'uid': None, 'psw': None}

# connect to mongoDB
client = pymongo.MongoClient(host='localhost', port=27017)
# find the database
db = client.user_list
# find the collections under the database
collection = db.user
collection2 = db.test
#
# new_user = {
#     'uid': '1001',
#     'psw': '12345'
# }

# collection.insert_one(new_user)


def check_list(inputList):
    # test the vulnerabilities according to options
    for i in inputList:
        # do test things
        if i == 'R_XSS':
            print('R_XSS chosen')
            url = "http://127.0.0.1:5001/main_page?input=123"
            r_test = Test(url, 'xss')
        elif i == 'S_XSS':
            print('S_XSS chosen')
        elif i == 'SSTI':
            print('SSTI chosen')


# encrypt the text with MD5
def encrypt_md5(text):
    ciphertext = hashlib.md5(text.encode(encoding='UTF8')).hexdigest()
    return ciphertext


# Welcome/Login page 登录/欢迎界面
@app.route('/', methods=['GET', 'POST'])
def welcome():
    app.logger.info('Login Page Loaded')

    if request.method == 'POST':
        # invocation_time = request.form.get('invocation')
        # response_time = request.form.get('response')
        # print('invoke: ' + invocation_time + ' RESPONSE: ' + response_time)
        start_time = time.perf_counter()
        uid = request.form.get('uid')   # get the input id
        psw = request.form.get('upsw')  # get the input password

        # check if this is a valid account
        check = collection.find_one({'uid': uid})
        # not found, thus no such an account
        if check is None:
            flash("Account Doesn't Exist!")

        # account exists, check the password
        elif check['psw'] == encrypt_md5(psw):
            currentUser['uid'] = uid
            currentUser['psw'] = psw
            app.logger.info('Main Page Open Start')
            end_time = time.perf_counter()
            time_used = (end_time - start_time) * 1000
            ta = float('%.2f' % time_used)
            test_data = {
                'func_time': ta,
                'user': uid
            }
            collection2.insert_one(test_data)
            print('Time Used: ' + str(ta) + ' ms')
            print('Full time: ' + str(time_used) + "ms")
            return redirect('/main_page')

        # wrong password
        else:
            app.logger.info('Login Page Reload Start')
            flash("Wrong Password!")

    app.logger.info('test1111111')
    return render_template('login.html')


# register page 注册
@app.route('/register', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        name = request.form.get('uName')
        psw = request.form.get('uPsw')

        if name and psw:
            # check if the same id exists in the DB
            check = collection.find_one({'uid': name})

            # exist: invalid
            if check:
                flash("Account Exists!")

            # not exist: store and back to log in
            else:
                psw = encrypt_md5(psw)
                new_user = {
                    'uid': name,
                    'psw': psw
                }
                collection.insert_one(new_user)
                return redirect('/')
    return render_template('reg.html')


@app.route('/main_page', methods=['GET', 'POST'])
def main_page():
    app.logger.info('Main Page Loaded')
    if request.method == 'POST':
        input = request.form.get('input')
        return 'Your input is: ' + str(input)
    # 一个思路：XSS主要由于GET请求的参数内容直接显示在URL中，因此form传参需要使用GET类型来确保可以直接使用脚本进行攻击测试
    # elif request.method == 'GET':
    #     input = request.form.get('input')
    #     return 'Your input is: ' + str(input)
    return render_template('main.html', user=currentUser)


@app.route('/main_page/ssti_test')
def hello_ssti():
    person = {
        'name': 'John',
        'age': '20',
        'password': 'abc123'
    }
    if request.args.get('name'):
        person['name'] = request.args.get('name')

    template = '<h2>%s</h2>' % person['name']
    return render_template_string(template, person=person)

#   http://127.0.0.1:5001/main_page/ssti_test?name={{12345}}
#   http://127.0.0.1:5001/main_page/ssti_test?name={{person.password}}
#   http://127.0.0.1:5001/main_page/ssti_test?name={{config}}


#   http://127.0.0.1:5001/dev
@app.route('/dev')
def device():
    with open("devices.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
        print(type(data))

    return render_template('t.html')


@app.route('/dev/router1', methods=['GET', 'POST'])
def r01():
    if request.method == 'POST':
        testList = request.values.getlist("t1")
        print(testList)
        print(type(testList))
        check_list(testList)

    return render_template('router1.html')


@app.route('/main/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'Current User {username}'


if __name__ == '__main__':
    handler = logging.FileHandler('test.log', encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run(port=5001)
