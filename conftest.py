import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser',
                        action='store',
                        help='select browser chrome or firefox',
                        default='chrome')
    parser.addoption('--language',  
                        action='store', 
                        default="ru",
                        help="Choose language: ru or en")

# Запуск произвожу только в Chrome, код подрезан по сравнению с предыдущими шагами
# Проверяется работоспособность кода для разных языков. 
# В задании не проверяю кросс-браузерность и обязательный запуск на Firefox.

@pytest.fixture(scope="function")
def browser(request):
    browser = request.config.getoption('browser')
    user_language = request.config.getoption("language")
    if browser == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser

    browser.quit()