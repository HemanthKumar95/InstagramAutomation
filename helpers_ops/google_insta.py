
from seleniumbase import BaseCase

class GoogleInsta:

    @staticmethod
    def navigate_to_insta(sbase: BaseCase):
        print(sbase.get_title())
        # sbase.send_keys('//input[@name="q"]', "Instagram Login")
        # sbase.click('//div[@class="FPdoLc tfB0Bf"]//input[@name="btnK"]')
        sbase.wait(5)
        sbase.click('//h3[text() = "Login • Instagram"]//parent::a')
