import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language',  
                        action='store', 
                        default=None,
                        help="Choose language: ru or en")

# Запуск произвожу только в Chrome, код подрезан по сравнению с предыдущими шагами
# Проверяется работоспособность кода для разных языков. 
# В задании не проверяю кросс-браузерность и обязательный запуск на Firefox.

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print(f"\nstart Chrome browser for test on language {user_language}")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()