from flask import Flask, render_template, request, redirect

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


@app.route('/mainPage')
def main_page():
    return render_template('main.html', user=currentUser)


if __name__ == '__main__':
    app.run(port=5001)
