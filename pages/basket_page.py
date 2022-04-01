from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_itemts_in_basket(self):
        """Проверка, что КОРЗИНА ПУСТА, что в ней не появился элемент с товаром"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ELEMENT), "В корзине есть товар. А не должно быть"

    def should_be_message_null_basket(self):
        """"Проверка что есть сообщение ВАША КОРЗИНА ПУСТА"""
        msg = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text.strip("Продолжить покупки")
        assert msg == "Ваша корзина пуста", "Нет сообщения ВАША КОРЗИНА ПУСТА"
