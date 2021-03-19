from seleniumbase import BaseCase

from constants import INSTAGRAM_URL
from insta_pages.Login import Login
from insta_pages.Profile import Profile
from insta_pages.HomePage import HomePage
from helpers_ops.google_insta import GoogleInsta

class AutomateLogin(BaseCase):
    go_with_last_user = False

    def login(self, username, password):

        self.open(INSTAGRAM_URL)
        GoogleInsta.navigate_to_insta(self)
        print(self.get_title())
        if self.is_element_present(Login.login_last_user) and self.go_with_last_user:
            Login.login_as_last_user(self)
        elif self.is_element_present(Login.login_last_user) and not self.go_with_last_user:
            self.click(Login.switch_accounts)
            Login.login_using_credentials(self, username, password)
        elif not self.go_with_last_user:
            Login.login_using_credentials(self, username, password)
        else:
            Login.login_with_facebook(self, username, password)
        self.wait(5)

        HomePage.presence_not_now(self)
        HomePage.presence_not_now(self)
        self.wait(10)

    def search_and_like_all_posts(self, username: str):

        search_word = username
        HomePage.search_profile(self, search_word)
        # self.wait_for_element_visible(Profile.insta_name)
        count_posts = int(Profile.get_no_of_posts(self))

        if count_posts < 25:
            max_limit = count_posts
        else:
            max_limit = 25

        if count_posts != 0 and not Profile.check_private_profile(self):
            self.wait(2)
            Profile.click_on_latest_post(self)
            Profile.like_all_posts(self, max_limit)
        else:
            print('The number of posts in the profile: ' + str(count_posts))
            print('Profile private: ' + str(Profile.check_private_profile(self)))
