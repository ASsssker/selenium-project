from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_be_basket_page(self):
        assert "basket" in self.browser.current_url, "The current page was expected to be the basket page."

    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_basket), "Basket is not empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "No message found indicating that the basket is empty"