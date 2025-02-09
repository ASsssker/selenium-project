from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        s = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_be_notification_successful_addition(self):
        assert self.is_element_present(*ProductPageLocators.CART_ADD_SUCCESS_ALERTS), "Product success add to card alert is not presented"

    @property
    def cart_price(self) -> float:
        assert self.is_element_present(*ProductPageLocators.CART_PRICE), "Cart price is not presented"
        cart_price_text =  self.browser.find_element(*ProductPageLocators.CART_PRICE).text.strip()
        return float(cart_price_text[:len(cart_price_text)-1].replace(",", "."))

    @property
    def success_add_to_card_text(self) ->str:
        return self.browser.find_element(*ProductPageLocators.CART_ADD_SUCCESS_ALERTS).text.strip()

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
