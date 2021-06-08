from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
import time


@pytest.mark.parametrize("number", ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    pages = ProductPage(browser, link)
    pages.open()
    pages.should_not_be_success_message()
    # pages.should_be_another_link()
    pages.should_be_add_butter()
    pages.add_to_basket()
    time.sleep(1)
    pages.should_be_alert_adding_good()
    pages.should_be_alert_basket_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    pages = ProductPage(browser, link)
    pages.open()
    pages.add_to_basket()
    pages.guest_cant_see_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    pages = ProductPage(browser, link)
    pages.open()
    pages.guest_cant_see_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    pages = ProductPage(browser, link)
    pages.open()
    pages.add_to_basket()
    pages.message_disappeared_after_adding_product_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    pages = ProductPage(browser, link)
    pages.open()
    pages.go_to_basket()
    pages.should_not_be_products_in_the_basket()

