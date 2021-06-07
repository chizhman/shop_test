from .pages.product_page import ProductPage
import time

link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    pages = ProductPage(browser, link)
    pages.open()
    pages.should_be_add_butter()
    pages.add_to_basket()
    time.sleep(1)
    pages.should_be_alert_adding_good()
    pages.should_be_alert_basket_price()