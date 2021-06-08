from selenium import webdriver
from .base_page import BasePage
from .locators import *MainPageLocator


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocator.LOGIN_LINK), "Login is not presented"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPage.LOGIN_FORM), "There is no login form on this page"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPage.REGISTER_FORM), "There is no register form on this page"
        assert True

    def register_new_user(self, email, password):
        email_form = self.login.find_element(*LoginPage.EMAIL_FORM)
        email_form.sendKeys(f"{email}")
        password_form = self.login.find_element(*LoginPage.PASS_FORM)
        password_form.sendKeys(f"{password}")
        confirmation_pass_form = self.login.find_element(*LoginPage.CONF_PASS_FORM)
        confirmation_pass_form.sendKeys(f"{password}")