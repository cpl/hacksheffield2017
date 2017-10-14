import requests
from pprint import pprint

API = 'https://api.github.com/%s'
HEADER = {'Accept': 'application/vnd.github.v3+json'}


def help():
    return requests.get(API % '', HEADER)


def user_list(id):
    r = requests.get(API % 'users?since=%d' % id, HEADER).json()
    print r


def user_list_repos(user):
    return requests.get(API % 'users/%s/repos' % user, HEADER)


def repo_search(query):
    return requests.get(API % 'search/repositories?q=%s' % query, HEADER)


def repo_languages(user, repo):
    return requests.get(API % 'repos/%s/%s/languages' % (user, repo), HEADER)


if __name__ == '__main__':
    # pprint(help().json())
    # print list_repos('thee-engineer').json()
    # pprint(search_repo('sheffield').json())
    # pprint(repo_languages('thee-engineer', 'cryptor').json())
    user_list(145)
