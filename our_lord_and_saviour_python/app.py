from flask import Flask, render_template, request
from github_api import GithubUser

app = Flask('git connect')

MATCHED_PROFILES = {}
ghuser = None


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def handle_data():
    global ghuser
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            ghuser = GithubUser(username, password)
        except Exception:
            return render_template('login.html', err='FUCKING TRY AGAIN TWAT!')

        if MATCHED_PROFILES.get(username,None) is None:
            MATCHED_PROFILES[username] = ([],[])
        else:
            ghuser.active_matches = MATCHED_PROFILES[username][1]

        return render_template('user.html', username=username, userrepos=len(ghuser.matches))
    elif request.method == 'GET':
        return render_template('login.html', err='')
    else:
        return 'BA MUI, GET sau POST'


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/explore', methods=['GET', 'POST'])
def dislike_love():
    global ghuser
    return ghuser.username
    if request.method == 'POST':
        if request.form['submit'] == 'dislike':
            return 'miel'
        elif request.form['submit'] == 'love':
            return 'love'
        else:
            return 'unvalid'
    elif request.method == 'GET':
        return render_template("explore.html")
    else:
        return 'BA MUI, GET sau POST'


if __name__ == '__main__':
    app.run()