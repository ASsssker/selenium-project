import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                    help="Choose a language")


@pytest.fixture(scope="function")
def browser(request) -> WebDriver:
    from selenium import webdriver

    lang = request.config.getoption("language")
    if lang is None:
        raise pytest.UsageError(f"--language only the following values ​​are allowed: {",".join([i[0] for i in LANGUAGES])}")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=options)
    def browser_quit():
        browser.quit()

    request.addfinalizer(browser_quit)

    return browser

