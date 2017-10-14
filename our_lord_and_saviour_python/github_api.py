import requests


API = 'https://api.github.com/%s'
HEADER = {'Accept': 'application/vnd.github.v3+json'}


class GithubUser(object):

    def __init__(self, username, password):
        self.apiman = APIManager(username, password)

        user = self.apiman.get('user').json()
        self.username = username
        self.avatar = user['avatar_url']
        self.location = user['location']
        self.bio = user['bio']
        self.pub_repo_count = user['public_repos']
        self.prv_repo_count = user['total_private_repos']
        self.pub_gist_count = user['public_gists']
        self.followers_count = user['followers']
        self.following_count = user['following']

        self.languages = {}
        self.owned_repos = []
        self.external_repos = []
        repos = self.apiman.get('user/repos').json()
        for repo in repos:
            if repo['owner']['login'] == self.username:
                self.owned_repos.append(repo)
                languages = self.apiman.get('repos/%s/%s/languages' % (self.username, repo['name'])).json()

                for key, value in languages.items():
                    if self.languages.get(key, None) is None:
                        self.languages[key] = value
                    else:
                        self.languages[key] += value
                else:
                    self.external_repos.append(repo)

        print self.languages


class APIManager(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get(self, req):
        return requests.get(API % req, HEADER, auth=(self.username, self.password))

    def rate_limit(self):
        return self.get('rate_limit')

    def user_list(self, id):
        return self.get('users?since=%d' % id)

    def user_list_repos(self, user):
        return self.get('users/%s/repos' % user)

    def self_list_repos(self):
        return self.get('user/repos')

    def repo_search(self, query):
        return self.get('search/repositories?q=%s' % query)

    def repo_languages(self, user, repo):
        return self.get('repos/%s/%s/languages' % (user, repo))


if __name__ == '__main__':
    pass
