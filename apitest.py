import requests
import datetime
from pprint import pprint

API = 'https://api.github.com/%s'
HEADER = {'Accept': 'application/vnd.github.v3+json'}


def help():
    return requests.get(API % '', HEADER)


def list_repos(user):
    return requests.get(API % 'users/%s/repos' % user, HEADER)


def search_repo(query):
    return requests.get(API % 'search/repositories?q=%s' % query, HEADER)


if __name__ == '__main__':
    # pprint(help().json())
    # print list_repos('thee-engineer').json()
    pprint(search_repo('sheffield').json())
