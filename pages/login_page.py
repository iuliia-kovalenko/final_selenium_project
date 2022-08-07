from .base_page import BasePage
from .locators import *
from .main_page import *


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "/login/" in login_url, "'login' not in current url"


        # assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        # assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There are no login form"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "There are no registration form"
