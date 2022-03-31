from pages.product_page import ProductPage


# @pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  pytest.param(
#                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                      marks=pytest.mark.xfail),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, url):
#     page = ProductPage(browser, url)
#     page.open()
#     product_page = ProductPage(browser, browser.current_url)
#     product_page.add_to_basket_product()
#     product_page.solve_quiz_and_get_code()
#     product_page.check_message_add_to_basket()


# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, url)
#     page.open()
#     page.add_to_basket_product()
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, url)
#     page.open()
#     page.should_not_be_success_message()
#
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, url)
#     page.open()
#     page.add_to_basket_product()
#     page.should_dissapear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


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
