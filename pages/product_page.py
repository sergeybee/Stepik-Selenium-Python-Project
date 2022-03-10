from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket_product(self):
        """Метод добавления товара в корзину"""
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()

    def check_message_add_to_basket(self):
        self.should_be_message_title_add_to_basket()
        self.should_be_message_price_to_basket()

    def should_be_message_title_add_to_basket(self):
        """Проверка: название товара в сообщении совпадает с названием в корзине"""
        title_product = self.browser.find_element(*ProductPageLocators.TITLE_PRODUCT).text
        message_title = self.browser.find_element(ProductPageLocators.MESSAGE_AFTER_ADD_TO_BASKET).text
        assert title_product in "The shellcoder's handbook был добавлен в вашу корзину.", "MESSAGE TITLE AFTER ADD TO CART IS NOT FOUND"

    def should_be_message_price_to_basket(self):
        """Проверка: цена товара в сообщении совпадает с ценой в корзине"""
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        message_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_AFTER_ADD_TO_BASKET).text
        assert price_product in "Стоимость корзины теперь составляет 9,99 £", "MESSAGE PRICE ADD TO CART IS NOT FOUND"
