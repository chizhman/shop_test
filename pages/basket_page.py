from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IS_IN_BASKET), "We see the product in the basket, but shouldn't"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET), "No text 'empty basket' or basket is not empty"