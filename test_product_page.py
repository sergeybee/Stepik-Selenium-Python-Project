from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                 pytest.param(
                                     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                     marks=pytest.mark.xfail),
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket_product()
    product_page.solve_quiz_and_get_code()
    product_page.check_message_add_to_basket()

# @pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, url):
#     # url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, url)
#     page.open()
#     product_page = ProductPage(browser, browser.current_url)
#     product_page.add_to_basket_product()
#     product_page.solve_quiz_and_get_code()
#     product_page.check_message_add_to_basket()


# def test_guest_can_add_product_to_basket(browser, url):
#     url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, url)
#     page.open()
#     product_page = ProductPage(browser, browser.current_url)
#     product_page.add_to_basket_product()
#     product_page.solve_quiz_and_get_code()
#     product_page.check_message_add_to_basket()

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
