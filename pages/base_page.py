from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class BasePage():
	def __init__(self, driver, base_url='http://getpocket.com/'):
		self.driver = driver
		self.base_url = base_url

	def click_button(self, method, locator):
		submit = self.driver.find_element(method, locator)
		submit.click()