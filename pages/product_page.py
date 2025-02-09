from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        s = self.browser.find_element(*ProductPageLocators.ADD_TO_basket_BUTTON).click()

    def should_be_notification_successful_addition(self):
        assert self.is_element_present(*ProductPageLocators.basket_ADD_SUCCESS_ALERTS), "Product success add to card alert is not presented"

    def should_not_be_notification_successful_addition(self):
        assert self.is_not_element_present(*ProductPageLocators.basket_ADD_SUCCESS_ALERTS), "Product success add to card alert is presented"

    def should_be_disappeared_notification_successful_addition(self):
        assert self.is_disappeared(*ProductPageLocators.basket_ADD_SUCCESS_ALERTS), "Product success add to card alert is not disappeared"

    @property
    def basket_price(self) -> float:
        assert self.is_element_present(*ProductPageLocators.basket_PRICE), "Basket price is not presented"
        basket_price_text =  self.browser.find_element(*ProductPageLocators.basket_PRICE).text.strip()
        return float(basket_price_text[:len(basket_price_text)-1].replace(",", "."))

    @property
    def success_add_to_card_text(self) ->str:
        return self.browser.find_element(*ProductPageLocators.basket_ADD_SUCCESS_ALERTS).text.strip()

    @property
    def product_name(self) -> str:
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()

    @property
    def price(self) -> float:
        assert self.is_element_present(*ProductPageLocators.PRICE), "Price is not presented"
        price_text = self.browser.find_element(*ProductPageLocators.PRICE).text.strip()
        return float(price_text[:len(price_text)-1].replace(",", "."))

    @property
    def promo(self) -> str:
        return self.get_query_param("promo")
