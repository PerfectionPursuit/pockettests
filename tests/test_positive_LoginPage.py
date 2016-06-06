from selenium import webdriver
from pages.LoginPage import LoginPage
import pytest

driver = webdriver.Firefox()
url = 'http://getpocket.com/login/'
home_url = 'queue'

def setup_function(function):
	driver.get(url)

def teardown_function(function):
	driver.close()

def test_positive_LoginPage():
	login_page = LoginPage(driver)
	login_page.login('trickytester@mailinator.com', 'qazwsx123')
	assert home_url in driver.current_url