import math

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class BasePage():

    def __init__(self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url

        self.browser.implicitly_wait(10)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how: str, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

        return True

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