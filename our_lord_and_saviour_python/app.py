from flask import Flask, render_template, request
from github_api import GithubUser
from pprint import pprint

app = Flask('git connect')

MATCHED_PROFILES = {}
ghuser = None


@app.route('/')
def hello():
    return render_template('app/index.html')


@app.route('/login', methods=['GET', 'POST'])
def handle_data():
    global ghuser
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            ghuser = GithubUser(username, password)
        except Exception:
            return render_template('app/index.html')

        if MATCHED_PROFILES.get(username, None) is None:
            MATCHED_PROFILES[username] = ([], [])
        else:
            ghuser.active_matches = MATCHED_PROFILES[username][1]

        # , username=ghuser.username, location=ghuser.location, bio=ghuser.bio, repocount=ghuser.repo_count, l1=ghuser.lang_name[0], l2=ghuser.lang_name[1], l3=ghuser.lang_name[2]
        return render_template('app/profile.html', user_name=ghuser.username, location=ghuser.location, bio=ghuser.bio, repo_count=ghuser.repo_count, lang0=ghuser.lang_name[0][0], lang1=ghuser.lang_name[1][0], lang2=ghuser.lang_name[2][0], match_count=len(ghuser.matches)-ghuser.mindex)
    elif request.method == 'GET':
        return render_template('app/index.html')
    else:
        return 'Please try again, this time using GET or POST'


@app.route('/profile')
def user():
    global ghuser
    if ghuser is None:
        return render_template('app/index.html')
    return render_template('app/profile.html', user_name=ghuser.username, location=ghuser.location, bio=ghuser.bio, repo_count=ghuser.repo_count, lang0=ghuser.lang_name[0][0], lang1=ghuser.lang_name[1][0], lang2=ghuser.lang_name[2][0], match_count=len(ghuser.matches)-ghuser.mindex)


@app.route('/explore', methods=['GET', 'POST'])
def dislike_love():
    global ghuser
    if ghuser is None:
        return render_template('login.html', err='PLEASE LOG IN')

    pprint(MATCHED_PROFILES)

    if request.method == 'POST':
        if request.form['submit'] == 'dislike':
            pass  # do nothing
        elif request.form['submit'] == 'love':
            # matched user
            muser = ghuser.matches[ghuser.mindex-1]['login']
            if MATCHED_PROFILES.get(muser, None) is None:
                MATCHED_PROFILES[muser] = ([ghuser.username], [])
            elif muser in MATCHED_PROFILES[ghuser.username][0]:
                print '******* ******* SHITFUCK ******* *******'
                MATCHED_PROFILES[muser][1].append(ghuser.username)
                MATCHED_PROFILES[ghuser.username][1].append(muser)
        else:
            return 'unvalid'

        return render_template("explore.html", match_count=len(MATCHED_PROFILES[ghuser.username][1]), username=ghuser.get_match())
    elif request.method == 'GET':
        return render_template("explore.html", match_count=len(MATCHED_PROFILES[ghuser.username][1]), username=ghuser.get_match())
    else:
        return 'BA MUI, GET sau POST'


if __name__ == '__main__':
    app.run()
