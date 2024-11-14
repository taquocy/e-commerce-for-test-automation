from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang đăng ký
        self.open_register_button = (By.XPATH, "//a[@href='/signup']/button")  # Nút mở form đăng ký
        self.email_input = (By.NAME, "email")  # Trường email
        self.password_input = (By.NAME, "password")  # Trường mật khẩu
        self.confirm_password_input = (By.NAME, "passwordConfirm")  # Trường xác nhận mật khẩu
        self.submit_register_button = (By.XPATH, "//button[@type='submit']")  # Nút submit đăng ký
        self.success_message = (By.XPATH, "//div[contains(@class, 'success-message')]")  # Thông báo thành công

    def open_register_form(self):
        # Mở form đăng ký
        self.driver.find_element(*self.open_register_button).click()

    def enter_email(self, email):
        # Nhập email vào trường email
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        # Nhập mật khẩu vào trường mật khẩu
        self.driver.find_element(*self.password_input).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        # Nhập mật khẩu xác nhận vào trường xác nhận mật khẩu
        self.driver.find_element(*self.confirm_password_input).send_keys(confirm_password)

    def click_register_button(self):
        # Nhấn nút submit đăng ký
        self.driver.find_element(*self.submit_register_button).click()

    def check_registration_success(self):
        # Kiểm tra thông báo thành công sau khi đăng ký
        assert self.driver.find_element(*self.success_message).is_displayed()
