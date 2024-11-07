from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang register
        self.menu_register =  (By.XPATH, "//a[@href='/signup']/button")
        self.email_input = (By.XPATH, "//input[@name='email']")
        self.password_input = (By.XPATH, "//input[@name='password']")
        self.passwordConfirm_input = (By.XPATH, "//input[@name='passwordConfirm']")
        self.register_button = (By.XPATH, "//button[@type='submit']")

    def open_register_form(self):
        self.driver.find_element(*self.menu_register).click()

    def enter_email(self, username):
        self.driver.find_element(*self.email_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def enter_passwordConfirm(self, passwordConfirm):
        self.driver.find_element(*self.password_input).send_keys(passwordConfirm)

    def click_register(self):
        self.driver.find_element(*self.register_button).click()
