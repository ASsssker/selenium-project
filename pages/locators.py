from selenium.webdriver.common.by import By


class BasePageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button")


class ProductPageLocators():

    ADD_TO_basket_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    basket_ADD_SUCCESS_ALERTS = (By.XPATH, '//div[contains(@class, "alert-success")][1]/div')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    basket_PRICE = (By.CSS_SELECTOR, ".alert-info p strong")


class BasketPageLocators():

    PAGE_NAME = (By.CSS_SELECTOR, "div.page-header h1")
    PRODUCT_IN_basket = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
