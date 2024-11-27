from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang register
        self.menu_register =  (By.XPATH, "//a[@href='/signup']/button")
        self.email_input = (By.XPATH, "//input[@name='email']")
        self.password_input = (By.XPATH, "//input[@name='password']")
        self.passwordConfirm_input = (By.XPATH, "//input[@name='passwordConfirm']")
        self.register_button = (By.XPATH, "//button[@type='submit']")
        self.message_create_account_successfully = (By.XPATH, "//span[text()='Create account successfully']")

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

    def is_success_message_appeared(self):
        try:
            # Chờ đợi tối đa 10 giây cho thông báo "Add product successfully" xuất hiện
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.message_create_account_successfully)
            )
            print("Message 'Creating successfully' appeared!")
            return True
        except TimeoutException:
            print("Message 'Creating successfully' did not appear.")
            return False

    def get_error_message(self):
        # Locate the error message element and return its text
        error_element = self.driver.find_element(By.XPATH, "//*[@class and contains(concat(' ', normalize-space(@class), ' '), ' chakra-alert ')]")
        return error_element.text
    
    def get_title(self, ttle:str):
        title_locator = (By.XPATH, self.title % ttle)
        title_element = self.driver.find_element(*title_locator)
        return title_element.text

