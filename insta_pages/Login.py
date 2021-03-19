from seleniumbase import BaseCase 

class Login(BaseCase):

    login_username = '//input[@name="username"]'
    login_password = '//input[@name="password"]'

    login_submit = '//button[@type="submit"]'

    login_last_user='//*[contains(text(),"Continue")]'

    switch_accounts='//button[text()="Switch accounts"]'
    
    fb_login_username = "#email"
    fb_login_password = "#pass"
    fb_login_button = "//button"
    
    @staticmethod
    def login_as_last_user(sbase: BaseCase):
        sbase.click(Login.login_last_user)
        
    
    @staticmethod
    def login_using_credentials(sbase: BaseCase, username: str,password: str):
        
        sbase.type(Login.login_username,username)
        sbase.type(Login.login_password,password)
        sbase.click(Login.login_submit)
    
    @staticmethod
    def login_with_facebook(self,username: str,password: str):
        self.type(Login.fb_login_username,username)
        self.type(Login.fb_login_password,password)
        self.click(Login.fb_login_button)
        