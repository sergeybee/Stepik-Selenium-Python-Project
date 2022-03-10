from pages.product_page import ProductPage

import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket_product()
    product_page.solve_quiz_and_get_code()
    time.sleep(10)
    product_page.check_message_add_to_basket()

# def test_should_be_message_add_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_message_add_to_basket()

# def test_should_be_message_price_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_message_price_to_basket()

# pytest -v --tb=line --language=en test_main_page.py
