from bs4 import BeautifulSoup
from urllib.request import urlopen


class GithubUser:
    FORMAT_URL = "https://github.com/{}?page={}&tab={}"
    FOLLOWING_TAB = "following"
    FOLLOWERS_TAB = "followers"

    def __init__(self, username):
        self.username = username
        self.following = None
        self.followers = None

    def __get_users_from_raw(self, raw_users):
        users = []
        for user in raw_users:
            users.append(GithubUser(user.string))
        return users

    def __get_tab_users(self, tab, page=1):
        url = self.FORMAT_URL.format(self.username, page, tab)
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        raw_users = soup.find_all("span", class_="Link--secondary pl-1")
        return self.__get_users_from_raw(raw_users)

    def __get_full_users(self, tab):
        full_users = []
        page = 1
        print("Getting {} from user {}".format(tab, self.username), end="", flush=True)
        while True:
            users = self.__get_tab_users(tab, page)
            if len(users) == 0:
                break
            full_users = full_users + users
            print(".", end="", flush=True)
            page = page + 1
        print()
        return full_users

    def get_followers(self) -> list:
        if not self.followers:
            self.followers = self.__get_full_users(self.FOLLOWERS_TAB)
        return self.followers
    
    def get_followings(self) -> list:
        if not self.following:
            self.following = self.__get_full_users(self.FOLLOWING_TAB)
        return self.following

    def get_following_followers_diff(self) -> list:
        if not self.followers:
            self.followers = self.__get_full_users(self.FOLLOWERS_TAB)
        if not self.following:
            self.following = self.__get_full_users(self.FOLLOWING_TAB)
        return list(set(self.following) - set(self.followers))

    def print_following_followers_diff(self) -> None:
        following_followers_diff = self.get_following_followers_diff()
        print("people {} following but not following back:".format(self.username))
        for i, user in enumerate(following_followers_diff):
            print(f"\t{i+1}- " + user.username)

    def __str__(self) -> str:
        print(self.username)

    def __hash__(self) -> int:
        return hash(self.username)

    def __eq__(self, __o: object) -> bool:
        return self.username == __o.username
