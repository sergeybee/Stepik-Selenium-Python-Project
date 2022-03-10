from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException


url = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

driver = webdriver.Chrome()
driver.get(url)


def add_to_basket_product():
    """Метод добавления товара в корзину"""
    btn = driver.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
    btn.click()

def solve_quiz_and_get_code():
    alert = driver.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")

def should_be_message_title_add_to_basket():
    """Проверка: название товара в сообщении совпадает с названием в корзине"""
    title_product = driver.find_element(*ProductPageLocators.TITLE_PRODUCT).text
    message_title = driver.find_element(*ProductPageLocators.MESSAGE_AFTER_ADD_TO_BASKET).text
    assert title_product == message_title, "MESSAGE TITLE AFTER ADD TO CART IS NOT FOUND"
    # print(title_product, "=", message_title)


def should_be_message_price_to_basket():
    """Проверка: цена товара в сообщении совпадает с ценой в корзине"""
    price_product = driver.find_element(*ProductPageLocators.PRICE_PRODUCT).text
    message_price = driver.find_element(*ProductPageLocators.TOTAL_PRICE_AFTER_ADD_TO_BASKET).text
    assert price_product == message_price, "MESSAGE PRICE ADD TO CART IS NOT FOUND"
    # print(price_product, "=", message_price)


add_to_basket_product()
solve_quiz_and_get_code()
should_be_message_title_add_to_basket()
should_be_message_price_to_basket()
