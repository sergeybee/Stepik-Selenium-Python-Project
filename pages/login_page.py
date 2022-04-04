import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self):
        # Проверка, что находимся на странице логина
        assert "login" in self.browser.current_url, "This is not a login page"

    def should_be_login_form(self):
        # Проверка, что есть форма авторизации на странице
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "LOGIN FORM is not presented"

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "REGISTER FORM is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

        confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_password_field.clear()
        confirm_password_field.send_keys(password)

        reg_submit_btn = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BTN)
        reg_submit_btn.click()
        time.sleep(3)
