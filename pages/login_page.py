from .base_page import BasePage
from .locators import MainPageLocator, LoginPageLocator


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocator.LOGIN_LINK), "Login is not presented"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocator.LOGIN_FORM), "There is no login form on this page"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocator.REGISTER_FORM), "There is no register form on this page"
        assert True

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocator.EMAIL_FORM)
        email_form.send_keys(f"{email}")
        password_form = self.browser.find_element(*LoginPageLocator.PASS_FORM)
        password_form.send_keys(f"{password}")
        confirmation_pass_form = self.browser.find_element(*LoginPageLocator.CONF_PASS_FORM)
        confirmation_pass_form.send_keys(f"{password}")
        button = self.browser.find_element(*LoginPageLocator.REGISTRATION_BUTTON)
        button.click()