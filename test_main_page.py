import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


def test_text_on_add_to_cart_button(browser: webdriver.Chrome, lang_and_expected_text: tuple[str, str]):
    lang = lang_and_expected_text[0]
    expected_text = lang_and_expected_text[1]

    browser.get(f"http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/")
    WebDriverWait(browser, 10).until(EC.visibility_of_any_elements_located, (By.CSS_SELECTOR, "#add_to_basket_form"))
    button_elements =browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form button")
    
    assert len(button_elements) < 2, f"Expected one element but found {len(button_elements)} elements"
    assert len(button_elements) == 1, "Element not found" 

    actual_text = button_elements[0].text
    assert actual_text == expected_text, f"The text on the button is not as expected, expected '{expected_text}' but got '{actual_text}'"
    