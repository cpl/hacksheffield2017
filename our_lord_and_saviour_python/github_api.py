import requests


API = 'https://api.github.com/%s'
HEADER = {'Accept': 'application/vnd.github.v3+json'}


class GithubUser(object):

    def __init__(self, username, password):
        self.apiman = APIManager(username, password)

        user = self.apiman.get('user')
        if user.status_code == 401:
            raise Exception()
        else:
            user = user.json()
        self.username = username
        self.avatar = user['avatar_url']
        self.location = user['location'].replace(' ', '') if user['location'] is not None else 'UK'
        self.bio = user['bio'] if user['bio'] is not None else 'Default'
        self.repo_count = user['public_repos'] + user['total_private_repos']
        self.pub_gist_count = user['public_gists']
        self.followers_count = user['followers']
        self.following_count = user['following']

        self.languages = {}
        repos = self.apiman.get('user/repos').json()
        for repo in repos:
            languages = self.apiman.get('repos/%s/%s/languages' % (repo['owner']['login'], repo['name'])).json()
            for key, value in languages.items():
                if self.languages.get(key, None) is None:
                    self.languages[key] = value
                else:
                    self.languages[key] += value

        self.lang_name = self.languages.keys()

        request = 'search/users?q=location:%s repos:%d..%d type:%s followers:%d..%d '
        for lang in languages.keys():
            request += 'language:%s ' % lang.replace(' ', '')
        request += '&per_page=100'

        # print request
        # print request % (self.location, 0, self.repo_count+1000, 'user', 0, self.followers_count+2000)
        self.matches = self.apiman.get(request % (self.location, 0, self.repo_count+1000, 'user', 0, self.followers_count+2000)).json()['items']


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
