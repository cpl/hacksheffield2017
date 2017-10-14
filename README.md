# GitHub API spec

* All request must contain the following header:
    * `Accept`: `application/vnd.github.v3+json`
    * Send username:password with basic auth

* User login
    * GET `https://api.github.com/user`
    * Should return:
```
{
  "login": "thee-engineer",
  "id": 17101435,
  "avatar_url": "https://avatars1.githubusercontent.com/u/17101435?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/thee-engineer",
  "html_url": "https://github.com/thee-engineer",
  "followers_url": "https://api.github.com/users/thee-engineer/followers",
  "following_url": "https://api.github.com/users/thee-engineer/following{/other_user}",
  "gists_url": "https://api.github.com/users/thee-engineer/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/thee-engineer/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/thee-engineer/subscriptions",
  "organizations_url": "https://api.github.com/users/thee-engineer/orgs",
  "repos_url": "https://api.github.com/users/thee-engineer/repos",
  "events_url": "https://api.github.com/users/thee-engineer/events{/privacy}",
  "received_events_url": "https://api.github.com/users/thee-engineer/received_events",
  "type": "User",
  "site_admin": false,
  "name": "Alexandru-Paul Copil",
  "company": null,
  "blog": "thee-engineer.github.io",
  "location": "Manchester, UK",
  "email": "alexandru.p.copil@gmail.com",
  "hireable": true,
  "bio": "`from kitchen import coffee`",
  "public_repos": 20,
  "public_gists": 3,
  "followers": 8,
  "following": 19,
  "created_at": "2016-02-06T19:25:34Z",
  "updated_at": "2017-10-13T07:11:10Z",
  "private_gists": 0,
  "total_private_repos": 27,
  "owned_private_repos": 27,
  "disk_usage": 968366,
  "collaborators": 4,
  "two_factor_authentication": true,
  "plan": {
    "name": "developer",
    "space": 976562499,
    "collaborators": 0,
    "private_repos": 9999
  }
}
```

* User repo stats
    * GET `https://api.github.com/user/repos`
    * Should return a list [] of repos
    * A Repo looks like:
```
{
    "id": 102940672,
    "name": "aluminium",
    "full_name": "thee-engineer/aluminium",
    "owner": {
      "login": "thee-engineer",
      "id": 17101435,
      "avatar_url": "https://avatars1.githubusercontent.com/u/17101435?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/thee-engineer",
      "html_url": "https://github.com/thee-engineer",
      "followers_url": "https://api.github.com/users/thee-engineer/followers",
      "following_url": "https://api.github.com/users/thee-engineer/following{/other_user}",
      "gists_url": "https://api.github.com/users/thee-engineer/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/thee-engineer/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/thee-engineer/subscriptions",
      "organizations_url": "https://api.github.com/users/thee-engineer/orgs",
      "repos_url": "https://api.github.com/users/thee-engineer/repos",
      "events_url": "https://api.github.com/users/thee-engineer/events{/privacy}",
      "received_events_url": "https://api.github.com/users/thee-engineer/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": true,
    "html_url": "https://github.com/thee-engineer/aluminium",
    "description": null,
    "fork": false,
    "url": "https://api.github.com/repos/thee-engineer/aluminium",
    "forks_url": "https://api.github.com/repos/thee-engineer/aluminium/forks",
    "keys_url": "https://api.github.com/repos/thee-engineer/aluminium/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/thee-engineer/aluminium/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/thee-engineer/aluminium/teams",
    "hooks_url": "https://api.github.com/repos/thee-engineer/aluminium/hooks",
    "issue_events_url": "https://api.github.com/repos/thee-engineer/aluminium/issues/events{/number}",
    "events_url": "https://api.github.com/repos/thee-engineer/aluminium/events",
    "assignees_url": "https://api.github.com/repos/thee-engineer/aluminium/assignees{/user}",
    "branches_url": "https://api.github.com/repos/thee-engineer/aluminium/branches{/branch}",
    "tags_url": "https://api.github.com/repos/thee-engineer/aluminium/tags",
    "blobs_url": "https://api.github.com/repos/thee-engineer/aluminium/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/thee-engineer/aluminium/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/thee-engineer/aluminium/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/thee-engineer/aluminium/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/thee-engineer/aluminium/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/thee-engineer/aluminium/languages",
    "stargazers_url": "https://api.github.com/repos/thee-engineer/aluminium/stargazers",
    "contributors_url": "https://api.github.com/repos/thee-engineer/aluminium/contributors",
    "subscribers_url": "https://api.github.com/repos/thee-engineer/aluminium/subscribers",
    "subscription_url": "https://api.github.com/repos/thee-engineer/aluminium/subscription",
    "commits_url": "https://api.github.com/repos/thee-engineer/aluminium/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/thee-engineer/aluminium/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/thee-engineer/aluminium/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/thee-engineer/aluminium/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/thee-engineer/aluminium/contents/{+path}",
    "compare_url": "https://api.github.com/repos/thee-engineer/aluminium/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/thee-engineer/aluminium/merges",
    "archive_url": "https://api.github.com/repos/thee-engineer/aluminium/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/thee-engineer/aluminium/downloads",
    "issues_url": "https://api.github.com/repos/thee-engineer/aluminium/issues{/number}",
    "pulls_url": "https://api.github.com/repos/thee-engineer/aluminium/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/thee-engineer/aluminium/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/thee-engineer/aluminium/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/thee-engineer/aluminium/labels{/name}",
    "releases_url": "https://api.github.com/repos/thee-engineer/aluminium/releases{/id}",
    "deployments_url": "https://api.github.com/repos/thee-engineer/aluminium/deployments",
    "created_at": "2017-09-09T08:48:28Z",
    "updated_at": "2017-09-09T08:59:37Z",
    "pushed_at": "2017-09-09T08:59:36Z",
    "git_url": "git://github.com/thee-engineer/aluminium.git",
    "ssh_url": "git@github.com:thee-engineer/aluminium.git",
    "clone_url": "https://github.com/thee-engineer/aluminium.git",
    "svn_url": "https://github.com/thee-engineer/aluminium",
    "homepage": null,
    "size": 15,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "Python",
    "has_issues": true,
    "has_projects": true,
    "has_downloads": true,
    "has_wiki": true,
    "has_pages": false,
    "forks_count": 0,
    "mirror_url": null,
    "open_issues_count": 0,
    "forks": 0,
    "open_issues": 0,
    "watchers": 0,
    "default_branch": "master",
    "permissions": {
      "admin": true,
      "push": true,
      "pull": true
    }
  }
```

* Relevant repo stats:
    * "id": 102940672,
    * "name": "aluminium"
    * "private": true
        * less score for privat repos
    * "html_url": "https://github.com/thee-engineer/aluminium"
        * for linking the project? 
    * "fork": false
        * ignore forked projects
    * "url": "https://api.github.com/repos/thee-engineer/aluminium"
        * for extra repo details?
    * "languages_url": "https://api.github.com/repos/thee-engineer/aluminium/languages"
        * for list of langauges
    * "commits_url": "https://api.github.com/repos/thee-engineer/aluminium/commits{/sha}"
        * returns a list of commits, use count
    * "open_issues": 0
        * issues are GOOD!
    * "forks_count": 0
        * forks should give a high score
    * "stargazers_count": 0
        * stars counts, high score!
    * "size": 15
        * idk what this is :)
        * the higher, the better
    * "watchers_count": 0
        * high score
    * "has_wiki": true
        * +some score
    * "has_pages": false
        * +some score

* Languages request format
```
{
  "C": 591074,
  "C++": 75372,
  "Go": 67188,
  "Java": 30290,
  "Python": 30188,
  "Assembly": 28453,
  "M4": 25931,
  "Makefile": 6705,
  "Shell": 47
}
```
