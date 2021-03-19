from Insta_Automation.InstagramAutomation.insta_pages.HomePage import HomePage
from Insta_Automation.InstagramAutomation.insta_pages.Profile import Profile
from Insta_Automation.InstagramAutomation.automation_ops.AutomationLogin import AutomateLogin
from constants import LOGIN_DATA

class MainExecution(AutomateLogin):
    def test_execution(self):
        try:
            self.login(LOGIN_DATA['username'], LOGIN_DATA['password'])
            # HomePage.search_profile(self, 'tamil_memes')
            # self.wait_for_element_visible(Profile.insta_name)

            # self.search_and_like_all_posts('ramana_1506')
            # print(Profile.get_no_of_followers(self))
            # print(Profile.get_no_of_following(self))

            Profile.fetch_user_follow_data(self, 'gowti_photography')
            self.wait_for_element_visible(HomePage.followings_data, timeout=20)
            HomePage.get_all_followings_data(self)
            self.wait_for_element_visible(HomePage.followers_data, timeout=120)
            HomePage.get_all_followers_data(self)
            self.wait(30)
        finally:
            HomePage.logout_from_profile(self)
