from seleniumbase import BaseCase

from Insta_Automation.InstagramAutomation.helpers_ops import Insta_Helpers


class FacebookLoginPage():
    # Login page locators
    login_username = "#email"
    login_password = "#pass"
    login_button = "//button"

    @staticmethod
    def login_with_facebook(self, username: str, password: str):
        self.type(FacebookLoginPage.login_username, username)
        self.type(FacebookLoginPage.login_password, password)
        self.click(FacebookLoginPage.login_button)


class HomePage:
    insta_home = '//img[@alt="Instagram"]'
    not_now = "//*[text()='Not Now']"
    search_input = '//input[@type="text"]'
    log_out = '//*[text()="Log Out"]'
    profile_icon = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img'
    followings_data = '#followingsData'
    followers_data = '#followersData'

    @staticmethod
    def presence_not_now(sbase: BaseCase):
        if sbase.is_element_present(HomePage.not_now):
            sbase.click(HomePage.not_now)

    @staticmethod
    def logout(sbase: BaseCase):
        sbase.click(HomePage.profile_icon)
        sbase.wait_for_element_visible(HomePage.log_out)
        sbase.click(HomePage.log_out)

    @staticmethod
    def _get_search_icon(search_word: str) -> str:
        return f'//a[contains(@href,"{search_word}")]'

    @staticmethod
    def search_profile(sbase: BaseCase, search_word: str):
        sbase.type(HomePage.search_input, search_word)
        sbase.click(HomePage._get_search_icon(search_word), timeout=3)

    @staticmethod
    def logout_from_profile(sbase: BaseCase):
        sbase.click(HomePage.profile_icon)
        sbase.wait_for_element_visible(HomePage.log_out)
        if sbase.is_element_visible(HomePage.log_out):
            sbase.click(HomePage.log_out)

    @staticmethod
    def get_all_followers_data(sbase: BaseCase):
        if sbase.is_element_present(HomePage.followers_data):
            data = sbase.get_text(HomePage.followers_data)
            Insta_Helpers.write_data_to_file('followers.txt', data)

    @staticmethod
    def get_all_followings_data(sbase: BaseCase):
        if sbase.is_element_present(HomePage.followings_data):
            data = sbase.get_text(HomePage.followings_data)
            Insta_Helpers.write_data_to_file('followings.txt', data)
