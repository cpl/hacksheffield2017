from flask import Flask, render_template, request
from github_api import GithubUser

app = Flask('git connect')


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        ghuser = GithubUser(username, password)
        return render_template('user.html', username=username, userrepos=ghuser.languages)
    elif request.method == 'GET':
        return render_template('login.html')
    else:
        return 'BA MUI, GET sau POST'


@app.route('/user')
def user():
    return render_template('user.html')


if __name__ == '__main__':
    app.run()
