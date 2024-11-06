from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang đăng ký
        self.menu_register = (By.XPATH, "//a[@href='/register']/button")
        self.username_input = (By.NAME, "username")  # Tìm trường tên đăng nhập
        self.email_input = (By.NAME, "email")  # Tìm trường email
        self.password_input = (By.NAME, "password")  # Tìm trường mật khẩu
        self.confirm_password_input = (By.NAME, "confirm_password")  # Tìm trường xác nhận mật khẩu
        self.register_button = (By.XPATH, "//button[@type='submit']")  # Nút submit

    # Mở form đăng ký
    def open_register_form(self):
        self.driver.find_element(*self.menu_register).click()

    # Nhập tên đăng nhập
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    # Nhập email
    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    # Nhập mật khẩu
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    # Nhập lại mật khẩu để xác nhận
    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.confirm_password_input).send_keys(confirm_password)

    # Nhấn nút đăng ký
    def click_register(self):
        self.driver.find_element(*self.register_button).click()
