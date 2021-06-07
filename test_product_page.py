from .pages.product_page import ProductPage
import pytest
import time


@pytest.mark.parametrize("number", ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    pages = ProductPage(browser, link)
    pages.open()
    pages.should_not_be_success_message()
    pages.should_be_add_butter()
    pages.add_to_basket()
    time.sleep(1)
    pages.should_be_alert_adding_good()
    pages.should_be_alert_basket_price()