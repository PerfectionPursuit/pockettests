import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.user_page import UserPage


class TestLoginPage():
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
    
    @classmethod
    def teardown_class(cls):
        cls.driver.close()

    def setup_method(self, method):
        self.driver.get('http://getpocket.com/login/')
   
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
        assert login_page.email_error_text() == 'Please enter an email address or a username.'
        assert login_page.password_error_displayed()
        assert login_page.password_error_text() == 'Please enter a password.'

    def test_positive(self):
        self.home_url = 'queue'
        login_page = LoginPage(self.driver)
        login_page.login('trickytester@mailinator.com', 'qazwsx123')
        assert self.home_url in self.driver.current_url

    def test_positive1(self):
        login_page = LoginPage(self.driver)
        login_page.login('trickytester@mailinator.com', 'qazwsx123')
        user_page = UserPage()
        assert user_page.list_title_displayed()
