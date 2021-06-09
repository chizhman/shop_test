from selenium.webdriver.common.by import By


class MainPageLocator():
    BUTTON_TO_ADD = (By.CSS_SELECTOR, "button[value='Add to basket']")
    SWITCH_TO_BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")


class GoodAddLocator():
    NAME_GOOD = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_NAME_GOOD = (By.CSS_SELECTOR, ".alert-safe:nth-child(1) strong ")
    PRICE_GOOD = (By.CSS_SELECTOR, ".product_main > .price_color")
    ALERT_PRICE_GOOD = (By.CSS_SELECTOR, ".alert-safe:nth-child(3) strong ")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    PRODUCT_IS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary .basket-items")
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, ".content p")


class LoginPageLocator():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    CONF_PASS_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")