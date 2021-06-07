from .base_page import BasePage
from .locators import MainPageLocator, GoodAddLocator


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

