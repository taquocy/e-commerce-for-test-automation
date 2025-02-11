from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class LoginPage:
    def __init__(self, driver):
        """Khởi tạo trang đăng nhập với driver Selenium."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Đợi tối đa 10 giây

        # Xác định các phần tử trên trang login
        self.menu_login = (By.XPATH, "//a[@href='/signin']/button")
        self.menu_register = (By.XPATH, "//a[@href='/signup']/button")
        self.username_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.error_message = (By.XPATH, "//*[@class and contains(concat(' ', normalize-space(@class), ' '), ' chakra-alert ')]")
        self.title_xpath = "//h2[normalize-space(text())='%s']"

    def open_login_form(self):
        """Mở form đăng nhập."""
        self.wait.until(EC.element_to_be_clickable(self.menu_login)).click()

    def open_register_form(self):
        """Mở form đăng ký."""
        self.wait.until(EC.element_to_be_clickable(self.menu_register)).click()

    def enter_username(self, username):
        """Nhập tên đăng nhập vào ô email."""
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)

    def enter_password(self, password):
        """Nhập mật khẩu vào ô password."""
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

    def click_login(self):
        """Nhấn vào nút đăng nhập."""
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def get_error_message(self):
        """Lấy thông báo lỗi (nếu có)."""
        try:
            error_element = self.wait.until(EC.visibility_of_element_located(self.error_message))
            return error_element.text
        except TimeoutException:
            return None  # Không có thông báo lỗi

    def get_title(self, title: str):
        """Lấy tiêu đề trang dựa trên văn bản mong muốn."""
        try:
            title_locator = (By.XPATH, self.title_xpath % title)
            title_element = self.wait.until(EC.visibility_of_element_located(title_locator))
            return title_element.text
        except TimeoutException:
            return None
