from selenium import webdriver

from pages.base_page import BasePage
from locators.user_page_locators import UserPageLocators


class UserPage():
    def list_title_displayed(self):
        list_title = self.driver.find_element(
            *UserPageLocators.list_title)
        return list_title.is_displayed()