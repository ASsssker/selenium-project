from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_be_basket_page(self):
        assert "Корзина" == self.browser.find_element(*BasketPageLocators.PAGE_NAME).text, "The page title on the page does not match what is expected"

    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_basket), "Basket is not empty"

    def should_be_empty_basket_message(self):
        assert "Ваша корзина пуста" in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text, "No message found indicating that the basket is empty"