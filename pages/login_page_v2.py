from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Reuse WebDriverWait for consistency

        # Locators
        self.menu_login = (By.XPATH, "//a[@href='/signin']/button")
        self.username_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.email_error = (By.CSS_SELECTOR, "input[type='email'] + div")
        self.password_error = (By.CSS_SELECTOR, "input[type='password'] + div")

    def open_login_form(self):
        """Open the login form by clicking the menu login button."""
        menu_login = self.wait.until(EC.element_to_be_clickable(self.menu_login))
        menu_login.click()

    def enter_username(self, username):
        """Fill in the username input field."""
        self.wait.until(EC.presence_of_element_located(self.username_input)).send_keys(
            username
        )

    def enter_password(self, password):
        """Fill in the password input field."""
        self.wait.until(EC.presence_of_element_located(self.password_input)).send_keys(
            password
        )

    def click_login(self):
        """Click the login button."""
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def get_error_message(self):
        """Retrieve error messages from the form."""
        error_messages = []
        email_error = self._get_text_if_present(self.email_error)
        password_error = self._get_text_if_present(self.password_error)
        if email_error:
            error_messages.append(email_error)
        if password_error:
            error_messages.append(password_error)
        return " ".join(error_messages)

    def get_email_error_message(self):
        """Get email-specific error message."""
        return self._get_text_if_present(self.email_error)

    def get_password_error_message(self):
        """Get password-specific error message."""
        return self._get_text_if_present(self.password_error)

    def _get_text_if_present(self, locator):
        """Helper to retrieve text if the element is present, else return an empty string."""
        try:
            return self.driver.find_element(*locator).text.strip()
        except Exception:
            return ""
