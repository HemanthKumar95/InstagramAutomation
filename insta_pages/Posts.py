from seleniumbase import BaseCase


class Posts(BaseCase):
    like_post = '//section//*[@aria-label="Like"]'
    unlike_post = '//section//*[@aria-label="Unlike"]'
    comment_post = '//section//*[@aria-label="Comment"]'
    share_post = '//section//*[@aria-label="Share Post"]'
    post_a_comment = '//*[@aria-label="Add a comment…"]'
    post_after_comment = '//button[text()="Post"]'
    post_next = '//a[text()="Next"]'
    post_previous = '//a[text()="Previous"]'
    to_be_shared = '//input[@name="queryBox"]'
    post_close = '//*[@aria-label="Close"]/../..'

    @staticmethod
    def like_a_post(sbase: BaseCase):
        sbase.wait(1)
        if sbase.is_element_visible(Posts.like_post):
            sbase.click(Posts.like_post)

    @staticmethod
    def unlike_a_post(sbase: BaseCase):
        sbase.wait(1)
        if sbase.is_element_visible(Posts.unlike_post):
            sbase.click(Posts.unlike_post)

    @staticmethod
    def comment_on_post(sbase: BaseCase, message: str):

        if sbase.is_element_visible(Posts.post_a_comment):
            sbase.type(Posts.post_a_comment, message)
        sbase.click(Posts.post_after_comment)

    @staticmethod
    def share_the_post(sbase: BaseCase, profile_name: str):

        if sbase.is_element_visible(Posts.to_be_shared):
            sbase.type(Posts.to_be_shared, profile_name)

        sbase.assert_false(True)

    @staticmethod
    def move_to_next_post(sbase: BaseCase):
        if sbase.is_element_visible(Posts.post_next):
            sbase.click(Posts.post_next, delay=2)

    @staticmethod
    def move_to_previous_post(sbase: BaseCase):
        if sbase.is_element_visible(Posts.post_previous):
            sbase.click(Posts.post_previous)

    @staticmethod
    def close_the_post(sbase: BaseCase):
        if sbase.is_element_visible(Posts.post_close):
            sbase.click(Posts.post_close)
