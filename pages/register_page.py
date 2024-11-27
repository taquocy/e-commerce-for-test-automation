from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang register
        self.menu_register =  (By.XPATH, "//a[@href='/signup']/button")
        self.login_heading =  (By.XPATH, "//h2[text()='Signin']")
        self.email_input = (By.NAME, "email")  # Tìm trường username
        self.password_input = (By.NAME, "password")  # Tìm trường password
        self.confirm_password_input = (By.NAME, "passwordConfirm")  # Tìm trường confirm password
        self.register_button = (By.XPATH, "//button[@type='submit']")  # Nút submit
        self.error_message=(By.XPATH,"//div[@data-status='error' and @role='alert']")

    def open_register_form(self):
        self.driver.find_element(*self.menu_register).click()
    # Hàm để nhập tên đăng nhập
    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    # Hàm để nhập mật khẩu
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
    
    # Hàm để nhập xác nhận mật khẩu
    def enter_confirm_password(self, password):
        self.driver.find_element(*self.confirm_password_input).send_keys(password)

    # Hàm để nhấn nút register
    def click_register(self):
        self.driver.find_element(*self.register_button).click()

    def get_error_message(self):
        error_element = self.driver.find_element(By.XPATH, "//*[@class and contains(concat(' ', normalize-space(@class), ' '), ' chakra-alert ')]")
        return error_element.text

    def check_form_error(self, expected_message):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.error_message)
            )
            print(f"Message '{expected_message}' appeared!")
            return True
        except TimeoutException:
            print(f"Message '{expected_message}' did not appear.")
            return False

    def check_register_success(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.login_heading)
            )
            print("The sign-up page loaded successfully.")
            return True
        except TimeoutException:
            print("Failed to load the sign-up page.")
            return False