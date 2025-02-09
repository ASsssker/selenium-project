import pytest

from selenium.webdriver.remote.webdriver import WebDriver

from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser: WebDriver, link: str):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_notification_successful_addition()
    
    expected_product_add_alert_text =f"{product_page.product_name} был добавлен в вашу корзину."
    actual_product_add_alert = product_page.success_add_to_card_text
    assert expected_product_add_alert_text == actual_product_add_alert, f"Expected product add alert is not equal to got: expected '{expected_product_add_alert_text}', got '{actual_product_add_alert}'"
    
    expected_product_price = product_page.price
    actual_cart_price = product_page.cart_price
    assert expected_product_price == actual_cart_price, f"The price of the basket is not equal to the expected: '{expected_product_price}', got '{actual_cart_price}'"
