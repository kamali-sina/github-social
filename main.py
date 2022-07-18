from sys import argv

from GithubUser import GithubUser

if len(argv) < 2:
    print("Usage: main.py <username>")
    exit(1)

username = argv[1]

github_user = GithubUser(username)
github_user.print_following_followers_diff()
