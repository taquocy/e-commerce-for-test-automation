from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang register
        self.menu_register = (By.XPATH, "//a[@href='/signup']/button")
        self.email_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.password_confirm_input = (By.NAME, "passwordConfirm")
        self.register_button = (By.XPATH, "//button[@type='submit']")
        self.error_message=(By.XPATH,"//div[@data-status='error' and @role='alert']")

    def open_register_form(self):
        self.driver.find_element(*self.menu_register).click()

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def enter_password_confirm(self, password_confirm):
        self.driver.find_element(*self.password_confirm_input).send_keys(password_confirm)

    def click_register(self):
        self.driver.find_element(*self.register_button).click()

    def check_form_input_error(self, expected_message):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.error_message)
            )
            print(f"Message '{expected_message}' appeared!")
            return True
        except TimeoutException:
            print(f"Message '{expected_message}' did not appear.")
            return False

    def check_load_register_page_success(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_input)
            )
            print("The sign-up page loaded successfully.")
            return True
        except TimeoutException:
            print("Failed to load the sign-up page.")
            return False