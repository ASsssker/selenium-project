import pytest
import time

from selenium.webdriver.remote.webdriver import WebDriver

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestUserAddToBasketFromProductPage():

    def setup(self, browser: WebDriver):
        ProductPage(browser, link).go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = f"{time.now()}dsadasd@mail.ru"
        passowrd = f"{time.now()}dsadawdawsadasdasd"
        login_page.register(email, passowrd)
        login_page.is_logged()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser: WebDriver):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_notification_successful_addition()
        
        product_page.should_be_product_name_contains_in_basket_alert()

        product_page.should_be_product_price_equal_basket_price()
    
    def test_user_cant_see_success_message(self, browser: WebDriver):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_notification_successful_addition()


@pytest.mark.parametrize('link', ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser: WebDriver, link: str):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_notification_successful_addition()
    
    product_page.should_be_product_name_contains_in_basket_alert()

    product_page.should_be_product_price_equal_basket_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser: WebDriver):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_notification_successful_addition()


def test_guest_cant_see_success_message(browser: WebDriver):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_notification_successful_addition()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser: WebDriver):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_disappeared_notification_successful_addition()


def test_guest_should_see_login_link_on_product_page(browser: WebDriver):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser: WebDriver):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser: WebDriver):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_basket_is_empty()
    basket_page.should_be_empty_basket_message()
