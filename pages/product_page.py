from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_basket_BUTTON).click()

    def should_be_notification_successful_addition(self):
        assert self.is_element_present(*ProductPageLocators.basket_ADD_SUCCESS_ALERTS), "Product success add to card alert is not presented"

    def should_not_be_notification_successful_addition(self):
        assert self.is_not_element_present(*ProductPageLocators.basket_ADD_SUCCESS_ALERTS), "Product success add to card alert is presented"

    def should_be_disappeared_notification_successful_addition(self):
        assert self.is_disappeared(*ProductPageLocators.basket_ADD_SUCCESS_ALERTS), "Product success add to card alert is not disappeared"

    def should_be_product_name_contains_in_basket_alert(self):
        expected_product_add_alert_text = self.product_name
        actual_product_add_alert = self.success_add_to_basket_text
        assert expected_product_add_alert_text in actual_product_add_alert, f"Expected product add alert is not contains: expected contains'{expected_product_add_alert_text}', got '{actual_product_add_alert}'"

    def should_be_product_price_equal_basket_price(self):
        expected_product_price = self.price
        actual_basket_price = self.basket_price
        assert expected_product_price == actual_basket_price, f"The price of the basket is not equal to the expected: '{expected_product_price}', got '{actual_basket_price}'"

    @property
    def basket_price(self) -> float:
        assert self.is_element_present(*ProductPageLocators.basket_PRICE), "Basket price is not presented"
        basket_price_text =  self.browser.find_element(*ProductPageLocators.basket_PRICE).text.strip().replace("£", "")
        return float(basket_price_text[:len(basket_price_text)-1].replace(",", "."))

    @property
    def success_add_to_basket_text(self) ->str:
        return self.browser.find_element(*ProductPageLocators.basket_ADD_SUCCESS_ALERTS).text.strip()

    @property
    def product_name(self) -> str:
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()

    @property
    def price(self) -> float:
        assert self.is_element_present(*ProductPageLocators.PRICE), "Price is not presented"
        price_text = self.browser.find_element(*ProductPageLocators.PRICE).text.strip().replace("£", "")
        return float(price_text[:len(price_text)-1].replace(",", "."))

    @property
    def promo(self) -> str:
        return self.get_query_param("promo")
