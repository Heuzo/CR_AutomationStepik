import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en or ru")
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture()
def browser(request):
    browser_language = request.config.getoption("language")
    options = Options()
    if browser_language == 'fr':
        options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
        browser = webdriver.Chrome(options=options)
    elif browser_language == 'es':
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be en or ru")
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
