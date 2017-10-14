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

    def help(self):
        return self.get('', HEADER)

    def user_list(self, id):
        return self.get('users?since=%d' % id)

    def user_list_repos(self, user):
        return requests.get('users/%s/repos' % user)

    def repo_search(self, query):
        return self.get('search/repositories?q=%s' % query)

    def repo_languages(self, user, repo):
        return self.get('repos/%s/%s/languages' % (user, repo))


if __name__ == '__main__':

    apiman = APIManager(
        'thee-engineer',
        'b5d386e6d72e0e78bfebb318886e272afd1688d5')

    pprint(apiman.rate().json())
