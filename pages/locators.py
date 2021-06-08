# from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPageLocator():
    ADD_BUTTON = (By.CSS_SELECTOR, "button[value='Add to basket']")
    SWITCH_TO_BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")

class GoodAddLocator():
    def should_be_right_alert_name_good(self):
        self.name_good()
        self.alert_name_good()

    def should_be_right_alert_price_good(self):
        self.price_good()
        self.alert_price_good()

    def should_be_name_good(self):
        NAME_GOOD = (By.CSS_SELECTOR, ".product_main h1")
        return NAME_GOOD

    def should_be_alert_name_good(self):
        ALERT_NAME_GOOD = (By.CSS_SELECTOR, ".alert-safe:nth-child(1) strong ")
        return ALERT_NAME_GOOD

    def should_be_price_good(self):
        PRICE_GOOD = (By.CSS_SELECTOR, ".product_main > .price_color")
        return PRICE_GOOD

    def should_be_alert_price_good(self):
        ALERT_PRICE_GOOD = (By.CSS_SELECTOR, ".alert-safe:nth-child(3) strong ")
        return ALERT_PRICE_GOOD


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators():
    PRODUCT_IS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary .basket-items")
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "")