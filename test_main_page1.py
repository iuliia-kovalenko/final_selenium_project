import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(5)


def test_should_be_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()



def test_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_login_form_and_link(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()



def test_register_form_and_link(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()