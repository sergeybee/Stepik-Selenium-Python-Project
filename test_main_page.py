import time

from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


# Тестирование наличия логин ссылки пользователя класс MainPage()
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#
# def test_guest_should_be_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    time.sleep(2)
    page.should_not_be_itemts_in_basket()
    page.should_be_message_null_basket()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    time.sleep(2)
    page.should_not_be_itemts_in_basket()
    page.should_be_message_null_basket()


# Тестирование страницы авторизации и регистрации пользователя класс LoginPage()
# def test_should_be_login_url(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     login_page = LoginPage(browser, link)
#     login_page.open()
#     login_page.should_be_login_url()
#
# def test_should_be_login_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     login_page = LoginPage(browser, link)
#     login_page.open()
#     login_page.should_be_login_form()
#
# def test_should_be_register_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     login_page = LoginPage(browser, link)
#     login_page.open()
#     login_page.should_be_register_form()
