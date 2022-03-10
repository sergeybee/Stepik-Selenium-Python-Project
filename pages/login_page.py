from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):        
        # проверка что находимся на странице логина
        assert "login" in self.browser.current_url, "This is not a login page"


    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "LOGIN FORM is not presented"

    def should_be_register_form(self):
        # проверкf, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "REGISTER FORM is not presented"