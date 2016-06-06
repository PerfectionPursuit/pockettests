from selenium import webdriver
from pages.LoginPage import LoginPage
from locators.LoginPageLocators import LoginPageLocators
import pytest


class TestLoginPage(object):
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.url = 'http://getpocket.com/login/'
        self.driver.get(self.url)

    def teardown_method(self, method):
        self.driver.close()

    def test_positive(self):
        self.home_url = 'queue'
        login_page = LoginPage(self.driver)
        login_page.login('trickytester@mailinator.com', 'qazwsx123')
        assert self.home_url in self.driver.current_url

    def test_blank_password(self):
        login_page = LoginPage(self.driver)
        login_page.login('trickytester@mailinator.com', '')
        assert login_page.password_error_displayed()
        assert login_page.password_error_text() == 'Please enter a password.'

    def test_blank_email(self):
        login_page = LoginPage(self.driver)
        login_page.login('', 'qazwsx123')
        assert login_page.email_error_displayed
        assert login_page.email_error_text() == 'Please enter an email address or a username.'

    def test_blank_fields(self):
        login_page = LoginPage(self.driver)
        login_page.login('', '')
        assert login_page.email_error_displayed
        # assert login_page.email_error_text() == 'Please enter an email address or a username.'
        assert login_page.password_error_displayed()
        assert login_page.password_error_text() == 'Please enter a password.'