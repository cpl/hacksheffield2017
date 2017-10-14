import requests
from pprint import pprint

API = 'https://api.github.com/%s'
HEADER = {'Accept': 'application/vnd.github.v3+json'}

# 


class APIManager(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get(self, req):
        return requests.get(API % req, HEADER, auth=(self.username, self.password))

    def rate(self):
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
