from .base_page import BasePage
from .locators import MainPageLocator, LoginPage
# import time


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocator.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)


# class MainPage(BasePage):
#     def __init__(self, *args, **kwargs):
#         super(MainPage, self).__init__(*args, **kwargs)