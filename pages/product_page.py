from .base_page import BasePage
from .locators import MainPageLocator, GoodAddLocator, BasePageLocators
import pytest


class ProductPage(BasePage):
    def add_to_basket(self):
        adding = self.browser.find_element(*MainPageLocator.BUTTON_TO_ADD)
        adding.click()
        self.solve_quiz_and_get_code()

    def should_be_add_butter(self):
        assert self.is_element_present(*MainPageLocator.BUTTON_TO_ADD), "The button 'Add to Basket' is not here"

    def should_be_alert_adding_good(self):
        assert self.browser.find_element(*GoodAddLocator.NAME_GOOD).text == \
        self.browser.find_element(*GoodAddLocator.ALERT_NAME_GOOD).text, \
                                         "The good name is not correct in alert"

    def should_be_alert_basket_price(self):
        assert self.browser.find_element(*GoodAddLocator.PRICE_GOOD).text == \
        self.browser.find_element(*GoodAddLocator.ALERT_PRICE_GOOD).text, \
                                  "The good price is not correct in alert"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*GoodAddLocator.ALERT_PRICE_GOOD), \
            "Success message is presented, but should not be"

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        pytest.xfail()
        assert self.is_not_element_present(*GoodAddLocator.ALERT_NAME_GOOD), \
            "Success message is on the page after adding"

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*GoodAddLocator.ALERT_PRICE_GOOD), \
            "Success message is on the initial page, not good"

    def message_disappeared_after_adding_product_to_basket(self):
        pytest.xfail()
        assert self.is_disappeared(*GoodAddLocator.ALERT_PRICE_GOOD), \
                      "Success message is not disappearing after adding product in the basket"

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
