from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Explicit wait for better stability

        # Locators
        self.menu_login = (By.XPATH, "//a[@href='/signin']/button")
        self.username_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def open_login_form(self):
        self.wait.until(EC.element_to_be_clickable(self.menu_login)).click()

    def enter_username(self, username: str):
        username_field = self.wait.until(EC.visibility_of_element_located(self.username_input))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password: str):
        password_field = self.wait.until(EC.visibility_of_element_located(self.password_input))
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def login(self, username: str, password: str):
        self.open_login_form()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
