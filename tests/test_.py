from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

#class LoginPageLocators():
login_button = (By.CSS_SELECTOR, 'input.btn.login-btn-email')
email_field = (By.ID, 'feed_id')
password_field = (By.ID, 'login_password')
password_error = (By.CLASS_NAME, 'error-bubble')

#class UserPageLocators():
list_title = (By.CSS_SELECTOR,
              'h2.queue_title.queue_title_main.queue_title_queue')

class BasePage(object):
	def __init__(self, driver):
		self.driver = driver

	def click_button(self, method, locator):
		button = self.driver.find_element(method, locator)
		button.click()
		

class LoginPage(BasePage):
	def open():


	def set_email(self, email):
		email_element = self.driver.find_element(*email_field)
		email_element.send_keys(email)

	def set_password(self, password):
		password_element = self.driver.find_element(*password_field)
		password_element.send_keys(password)

	def login(self, email, password):
		self.set_email(email)
		self.set_password(password)
		self.click_button(*login_button)

	def password_error_displayed(self):
		error_bubble = self.driver.find_element(*password_error)
		return error_bubble.is_displayed()

class TestLoginPage(object):
	home_url = 'queue'

	def setUp_method(self, method):
		self.driver = webdriver.Firefox()
		self.driver.get('http://getpocket.com/login/')

	def tearDown_method(self, method):
	 	self.driver.close()

	#Valid credentials
	def test_positive_loginpage(self):
		self.login_page = LoginPage(self.driver)
		login_page.login('trickytester@mailinator.com', 'qazwsx123')
		assert home_url in self.driver.current_url

	#password_error_alert = driver.find_element(*password_error)

	# Valid e-mail. Empty password.
	def test_negative_login(self):
		login_page = LoginPage(self.driver)
		login_page.login('trickytester@mailinator.com', '')
		self.driver.implicitly_wait(3)
		password_error_alert = self.driver.find_element(*password_error)
		assert login_page.password_error_displayed
		assert password_error_alert.text == 'Please enter a password.'
