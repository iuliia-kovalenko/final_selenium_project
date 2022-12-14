from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        print(login_link)
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        login_link.click()


    def should_be_login_link(self):
        # assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        assert self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented"