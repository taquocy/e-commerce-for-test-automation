from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

        self.email_label = (By.XPATH, "//label[@for='field-:r1e:'']")
        self.email_input = (By.XPATH, "//input[@name='email']")

        self.password_label = (By.XPATH, "//label[@for='field-:r1f:']")
        self.password_input = (By.XPATH, "//input[@name='password']")

        self.update_profile_button = (By.XPATH, "//button[contains(text(),'Update Profile')]")  # Nút submit

        self.message_update_profile_successfully = (By.XPATH, "//span[text()='Update Profile successfully']")
        self.error_message_missing_special_characters = (By.XPATH, "//span[text()='Enter additional special characters!']")
        self.error_message_missing_capital_letters_and_special_characters = (By.XPATH, "//span[text()='Enter capital letters and special characters!']")
        self.error_message_password_cannot_be_blank = (By.XPATH, "//span[text()='Password cannot be blank!']")
        self.error_message_enter_capital_letters = (By.XPATH, "//span[text()='Enter capital letters!']")
        self.password_length_error_message = (By.XPATH, "//span[text()='Password must be more than 6 characters!']")

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_update_profile(self):
        self.driver.find_element(*self.update_profile_button).click()

    def is_success_message_appeared(self):
        try:
            # Chờ đợi tối đa 3 giây cho thông báo "Update profile successfully" xuất hiện
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self.message_update_profile_successfully)
            )
            print("Message 'Update profile successfully' appeared!")
            return True
        except TimeoutException:
            print("Message 'Update profile successfully' did not appear.")
            return False
    def is_error_message_missing_special_characters_appeared(self):
        try:
            # Chờ đợi tối đa 3 giây cho thông báo "Enter additional special characters!" xuất hiện
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self.error_message_missing_special_characters)
            )
            print("Message 'Enter additional special characters!' appeared!")
            return True
        except TimeoutException:
            print("Message 'Enter additional special characters!' did not appear.")
            return False
    def is_error_message_missing_capital_letters_and_special_characters_appeared(self):
        try:
            # Chờ đợi tối đa 3 giây cho thông báo "Enter capital letters and special characters!" xuất hiện
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self.error_message_missing_capital_letters_and_special_characters)
            )
            print("Message 'Enter capital letters and special characters!' appeared!")
            return True
        except TimeoutException:
            print("Message 'Enter capital letters and special characters!' did not appear.")
            return False
    def is_error_message_password_cannot_be_blank_appeared(self):
        try:
            # Chờ đợi tối đa 3 giây cho thông báo "Password cannot be blank!" xuất hiện
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self.error_message_password_cannot_be_blank)
            )
            print("Message 'Password cannot be blank!' appeared!")
            return True
        except TimeoutException:
            print("Message 'Password cannot be blank!' did not appear.")
            return False
    def is_error_message_enter_capital_letters_appeared(self):
        try:
            # Chờ đợi tối đa 3 giây cho thông báo "Enter capital letters!" xuất hiện
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self.error_message_password_cannot_be_blank)
            )
            print("Message 'Enter capital letters!' appeared!")
            return True
        except TimeoutException:
            print("Message 'Enter capital letters!' did not appear.")
            return False
    def is_password_length_error_message(self):
        try:
            # Chờ đợi tối đa 3 giây cho thông báo "Password must be more than 6 characters!" xuất hiện
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self.password_length_error_message)
            )
            print("Message 'Password must be more than 6 characters!' appeared!")
            return True
        except TimeoutException:
            print("Message 'Password must be more than 6 characters!' did not appear.")
            return False