from .base_page import BasePage
from .locators import MainPageLocator, GoodAddLocator
import pytest


class ProductPage(BasePage):
    def add_to_basket(self):
        adding = self.browser.find_element(*MainPageLocator.ADD_BUTTON)
        adding.click()
        self.solve_quiz_and_get_code()

    def should_be_add_butter(self):
        assert self.is_element_present(*MainPageLocator.ADD_BUTTON), "The button 'Add to Basket' is not here"

    def should_be_alert_adding_good(self):
        assert self.browser.find_element(*GoodAddLocator.should_be_name_good(GoodAddLocator)).text == \
        self.browser.find_element(*GoodAddLocator.should_be_alert_name_good(GoodAddLocator)).text, \
                                         "The good name is not correct in alert"

    def should_be_alert_basket_price(self):
        assert self.browser.find_element(*GoodAddLocator.should_be_price_good(GoodAddLocator)).text == \
        self.browser.find_element(*GoodAddLocator.should_be_alert_price_good(GoodAddLocator)).text, \
                                  "The good price is not correct in alert"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*GoodAddLocator.should_be_alert_price_good(GoodAddLocator)), \
            "Success message is presented, but should not be"

    # def should_be_another_link(self):
    #
    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        pytest.xfail()
        assert self.is_not_element_present(*GoodAddLocator.should_be_alert_name_good(GoodAddLocator)), \
            "Success message is on the page after adding"

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*GoodAddLocator.should_be_alert_price_good(GoodAddLocator)), \
            "Success message is on the initial page, not good"

    def message_disappeared_after_adding_product_to_basket(self):
        pytest.xfail()
        assert self.is_disappeared(*GoodAddLocator.should_be_alert_price_good(GoodAddLocator)), \
                      "Success message is not disappearing after adding product in the basket"
