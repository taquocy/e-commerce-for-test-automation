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
        self.profile_button = (By.XPATH, "//button[contains(@class, 'profile-button')]")

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

    def check_profile_page_display(self):
        """Kiểm tra xem trang hồ sơ có hiển thị sau khi đăng nhập không."""
        try:
            self.wait.until(EC.visibility_of_element_located(self.profile_button))
            return True
        except TimeoutException:
            return False

    def is_login_button_present(self):
        """Kiểm tra xem nút đăng nhập có hiển thị không."""
        try:
            return self.wait.until(EC.visibility_of_element_located(self.login_button)) is not None
        except TimeoutException:
            return False

    def is_password_field_masked(self):
        """Kiểm tra xem trường mật khẩu có bị ẩn hay không."""
        password_field = self.wait.until(EC.visibility_of_element_located(self.password_input))
        return password_field.get_attribute("type") == "password"

    def attempt_login_with_blank_fields(self):
        """Thử đăng nhập khi để trống cả email và mật khẩu."""
        self.click_login()
        return self.get_error_message()

    def attempt_login_with_invalid_email_format(self, email, password):
        """Thử đăng nhập với email không đúng định dạng."""
        self.enter_username(email)
        self.enter_password(password)
        self.click_login()
        return self.get_error_message()

    def attempt_login_with_wrong_credentials(self, email, password):
        """Thử đăng nhập với email và mật khẩu sai."""
        self.enter_username(email)
        self.enter_password(password)
        self.click_login()
        return self.get_error_message()

    def attempt_login_without_password(self, email):
        """Thử đăng nhập không nhập mật khẩu."""
        self.enter_username(email)
        self.click_login()
        return self.get_error_message()
