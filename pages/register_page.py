from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        # Define elements on the register page
        self.menu_register = (By.XPATH, "//a[@href='/signup']/button")  # Button to open registration form
        self.email_input = (By.NAME, "email")  # Email input field
        self.password_input = (By.NAME, "password")  # Password input field
        self.confirm_password_input = (By.NAME, "//*[@id='field-:r2:']")  # Confirm password field
        self.register_button = (By.XPATH, "//button[@type='submit']")  # Submit button

    # Method to open the registration form
    def open_register_form(self):
        self.driver.find_element(*self.menu_register).click()

    # Method to enter email
    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    # Method to enter password
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    # Method to confirm password
    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.confirm_password_input).send_keys(confirm_password)

    # Method to click the register button
    def click_register(self):
        self.driver.find_element(*self.register_button).click()
