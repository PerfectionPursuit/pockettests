from selenium.webdriver.common.by import By


class LoginPageLocators():
    email_field = (By.ID, 'feed_id')
    password_field = (By.ID, 'login_password')
    login_button = (By.CSS_SELECTOR, 'input.btn.login-btn-email')
    
    password_error = (By.CSS_SELECTOR,
                      'div.form-field.form-field-error>span.error-bubble')
    #password_error_text = (By.CSS_SELECTOR,
    #					   'span.error-bubble>span.error-msg')
    password_error_text = (By.XPATH, '//div[2]/span')
    email_error = (By.CSS_SELECTOR,
                   'span.error-bubble-twoliner')
    login_error = (By.CSS_SELECTOR, 'p.login-error')