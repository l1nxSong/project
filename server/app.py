from flask import Flask, render_template, request, redirect, render_template_string

import settings

app = Flask(__name__)
app.config.from_object(settings)

currentUser = {'uid': None, 'psw': None}


@app.route('/', methods=['GET', 'POST'])
def welcome():  # 登陆界面/ Login
    if request.method == 'POST':
        uid = request.form.get('uid')   # get the input id
        psw = request.form.get('upsw')  # get the input password

        if uid == '123' and psw == '123':   # set to current user
            # user = {'uid': uid, 'psw': psw}
            currentUser['uid'] = uid
            currentUser['psw'] = psw
            return redirect('/mainPage')

        else:   # reload
            return redirect('/')
    return render_template('login.html')


@app.route('/mainPage', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        input = request.form.get('input')
        return 'Your input is: ' + str(input)

    return render_template('main.html', user=currentUser)


@app.route('/mainPage/sstiTest')
def hello_ssti():
    person = {
        'name': 'hello',
        'age': '20',
        'password': 'abc123'
    }
    if request.args.get('name'):
        person['name'] = request.args.get('name')
    # changed
    template = '<h2>%s</h2>' % person['name']
    return render_template_string(template, person=person)

#   http://127.0.0.1:5001/mainPage/sstiTest?name={{12345}}
#   http://127.0.0.1:5001/mainPage/sstiTest?name={{person.password}}
#   http://127.0.0.1:5001/mainPage/sstiTest?name={{config}}

if __name__ == '__main__':
    app.run(port=5001)
