from selenium import webdriver
from pages.LoginPage import LoginPage
from locators.LoginPageLocators import LoginPageLocators
import pytest


driver = webdriver.Firefox()
url = 'http://getpocket.com/login/'


def setup_function(function):
    driver.get(url)


def teardown_function(function):
    driver.close()


def test_blank_password():
    login_page = LoginPage(driver)
    login_page.login('trickytester@mailinator.com', '')
    assert login_page.password_error_displayed()
    assert login_page.password_error_text() == 'Please enter a password.'


def test_blank_email():
    login_page = LoginPage(driver)
    login_page.login('', 'qazwsx123')
    assert login_page.email_error_displayed
    assert login_page.password_error_text() == 'Please enter an email address or a username.'