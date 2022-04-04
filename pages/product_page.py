from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators


class ProductPage(BasePage):

    def add_to_basket_product(self):
        """Метод добавления товара в корзину"""
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()

    def should_be_message_title_add_to_basket(self):
        """Проверка: название товара в сообщении совпадает с названием в корзине"""
        title_product = self.browser.find_element(*ProductPageLocators.TITLE_PRODUCT).text
        message_title = self.browser.find_element(*ProductPageLocators.MESSAGE_AFTER_ADD_TO_BASKET).text
        assert message_title == title_product, "Название товара не совпадает с названием товара в корзине"

    def should_be_message_price_to_basket(self):
        """Проверка: цена товара в сообщении совпадает с ценой в корзине"""
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        message_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_AFTER_ADD_TO_BASKET).text
        assert message_price == price_product, "Цена товара не совпадает с ценой товара в корзине"

    def check_message_add_to_basket(self):
        """Проверка: товар добавлен в корзину"""
        self.should_be_message_title_add_to_basket()
        self.should_be_message_price_to_basket()

    def should_not_be_success_message(self):
        """Проверка: что элемент не появился на странице"""
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_AFTER_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        """Проверка: что элемент не пропал, но должен был"""
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_AFTER_ADD_TO_BASKET), \
            "Success message is not disappeared, but should be"
