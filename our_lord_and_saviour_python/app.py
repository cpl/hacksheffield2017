from flask import Flask, render_template, request
from github_api import APIManager

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def handle_data():
    username = request.form['username']
    password = request.form['password']

    apiman = APIManager(username, password)

    return render_template(
        'index.html',
        test=apiman.rate().json())


if __name__ == '__main__':
    app.run()
