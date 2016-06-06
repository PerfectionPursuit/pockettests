from pages.BasePage import BasePage
from locators.LoginPageLocators import LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):
    password_error_message = 'Please enter a password.'
    email_error_message = 'Please enter an email address or a username.'
 
    def set_email(self, email):
        email_element = self.driver.find_element(
            *LoginPageLocators.email_field)
        email_element.send_keys(email)

    def set_password(self, password):
        password_element = self.driver.find_element(
            *LoginPageLocators.password_field)
        password_element.send_keys(password)

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_button(*LoginPageLocators.login_button)

    def password_error_displayed(self):
        error_bubble = self.driver.find_element(
            *LoginPageLocators.password_error)
        return error_bubble.is_displayed()

    def password_error_text(self):
        error = self.driver.find_element(
            *LoginPageLocators.password_error_text)
        return error.text

    def email_error_displayed(self):
        error_bubble = self.driver.find_element(*LoginPageLocators.email_error)
        return error_bubble.is_displayed()

    def email_error_text(self):
        error = self.driver.find_element(
            *LoginPageLocators.password_error_text)
        return error.text

    def login_error_displayed(self):
        error = self.driver.find_element(*LoginPageLocators.login_error)
        return error.is_displayed()

    def login_error_text(self):
        error = self.driver.find_element(*LoginPageLocators.login_error)
        return error.text
