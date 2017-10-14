from flask import Flask, render_template, request
from base64 import b64encode
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def handle_data():
    username = request.form['username']
    password = request.form['password']
    return render_template('index.html', test=b64encode(username + ':' + password))


if __name__ == '__main__':
    app.run()
