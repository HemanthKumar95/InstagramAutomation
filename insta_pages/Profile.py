from seleniumbase import BaseCase

from helpers_ops.helpers import Insta_Helpers
from insta_pages.Posts import Posts


class Profile(BaseCase):
    insta_username = '//h1'
    insta_name = '//h2'
    follow_button = '//button[text()="Follow"]'
    no_of_posts = '//*[text()=" posts"]//preceding-sibling::span'
    no_of_followers = '//*[text()=" followers"]//preceding-sibling::span'
    no_of_following = '//*[text()=" following"]//preceding-sibling::span'
    close_button = '//*[@aria-label="Close"]/../..'
    latest_post = '#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1) > a > div > div.KL4Bh > img'
    private_profile = '//h2[text()="This Account is Private"]'

    @staticmethod
    def get_no_of_posts(sbase: BaseCase):
        return sbase.get_text(Profile.no_of_posts, timeout=3).replace(",", "")

    @staticmethod
    def get_no_of_followers(sbase: BaseCase):
        follower = sbase.get_text(Profile.no_of_followers)
        if follower.endswith('k'):
            followers_count = follower.replace('k', '000')
        elif follower.endswith('m'):
            followers_count = follower.replace('m', '000000')
        else:
            followers_count = follower
        return int(followers_count.replace(",", ""))

    @staticmethod
    def get_no_of_following(sbase: BaseCase):
        following = sbase.get_text(Profile.no_of_following)
        if following.endswith('k'):
            followings_count = following.replace('k', '000')
        elif following.endswith('m'):
            followings_count = following.replace('m', '000000')
        else:
            followings_count = following
        return int(followings_count.replace(",", ""))

    @staticmethod
    def click_on_latest_post(sbase: BaseCase):
        action_on_latest_post = 'document.querySelector("' + \
                                Profile.latest_post + '").click();'
        sbase.execute_script(action_on_latest_post)

    @staticmethod
    def check_private_profile(sbase: BaseCase) -> bool:
        if sbase.is_element_visible(Profile.private_profile):
            return True
        return False

    @staticmethod
    def like_all_posts(sbase: BaseCase, max_limit: int):
        try:
            counter = 0
            while counter != max_limit:
                Posts.like_a_post(sbase)
                if not sbase.is_element_visible(Posts.post_next):
                    break
                Posts.move_to_next_post(sbase)
                counter += 1
        finally:
            Posts.close_the_post(sbase)

    @staticmethod
    def fetch_user_follow_data(sbase: BaseCase, username: str):
        Insta_Helpers.change_username(username)
        sbase.execute_script(open("/InstagramAutomation/helpers_ops/fetchUserFollowData.js").read())
