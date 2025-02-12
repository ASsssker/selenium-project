import math

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException

from .locators import BasePageLocators


class BasePage():

    def __init__(self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url

        self.browser.implicitly_wait(10)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def go_to_basket_page(self):
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented" 

    def is_element_present(self, how: str, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

        return True

    def is_not_element_present(self, how: str, what: str, timeout: float = 4) -> bool:
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_all_elements_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how: str, what: str, timeout: float = 4) -> bool:
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        
        return True
    
    def is_logged(self) -> bool:
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Not logged in"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_query_param(self, key: str) -> str:
        params = self._parse_query_params()
        if params is None:
            return ""
    
        return params.get(key, "")

    def _parse_query_params(self) -> dict[str, str]|None:
        url = self.url.split("/")
        if len(url) == 0:
            return None

        query_params = url[-1]
        if "?" not in query_params:
            return None

        return dict((param.split("=") for param in query_params.replace("?", "", 1).split("&")))