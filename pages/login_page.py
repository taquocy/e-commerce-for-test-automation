from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang login
        self.menu_login = (By.XPATH, "//a[@href='/signin']/button")
        self.username_input = (By.XPATH, "//input[@name='email']")  # Tìm trường username
        self.password_input = (By.XPATH, "//input[@name='password']")  # Tìm trường password
        self.login_button = (By.XPATH, "//button[@type='submit']")  # Nút submit
        self.login_error_message = (By.XPATH, "//div[text()='email or password not correct']")
        self.email_not_found_message = (By.XPATH, "//div[text()='The email address was not found.']")
        self.email_invalid_message = (By.XPATH, "//div[text()='\"email\" must be a valid email']")
        self.blank_email = (By.XPATH, "//input[@name='email' and @aria-invalid='true']")
        self.blank_password = (By.XPATH, "//input[@name='password' and @aria-invalid='true']")

    def open_login_form(self):
        self.driver.find_element(*self.menu_login).click()

    # Hàm để nhập tên đăng nhập
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    # Hàm để nhập mật khẩu
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    # Hàm để nhấn nút login
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    # Hàm kiểm tra thông báo lỗi
    def check_error_message(self):
        # Kiểm tra nếu 'email or password not correct' xuất hiện
        error_elements = self.driver.find_elements(*self.login_error_message)
        if error_elements:
            print("Message 'email or password not correct' appeared!")
            return "email_or_password_incorrect"

        # Kiểm tra nếu 'The email address was not found' xuất hiện
        not_found_elements = self.driver.find_elements(*self.email_not_found_message)
        if not_found_elements:
            print("Message 'The email address was not found' appeared!")
            return "email_not_found"

        # Kiểm tra nếu '"email" must be a valid email' xuất hiện
        invalid_email_elements = self.driver.find_elements(*self.email_invalid_message)
        if invalid_email_elements:
            print("Message '\"email\" must be a valid email' appeared!")
            return "invalid_email"

        blank_email_elements = self.driver.find_elements(*self.blank_email)
        if blank_email_elements:
            print("Message blank email")
            return "chua_nhap_email"

        blank_email_elements = self.driver.find_elements(*self.blank_password)
        if blank_email_elements:
            print("Message blank password")
            return "chua_nhap_password"

        print("No error message appeared.")
        return None
