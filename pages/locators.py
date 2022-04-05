from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT_BTN = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_AFTER_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner strong")
    TOTAL_PRICE_AFTER_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alert-success:first-child")


class BasketPageLocators:
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ELEMENT = (By.CLASS_NAME, "basket-items")


