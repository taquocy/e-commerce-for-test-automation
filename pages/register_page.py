from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang đăng ký
        self.menu_register = (By.XPATH, "//a[@href='/signup']/button")  # Nút mở form đăng ký
        self.email_input = (By.XPATH, "//input[@name='email']")  # Trường nhập email
        self.password_input = (By.XPATH, "//input[@name='password']")  # Trường nhập mật khẩu
        self.password_confirm_input = (By.XPATH, "//input[@name='passwordConfirm']")  # Trường xác nhận mật khẩu
        self.register_button = (By.XPATH, "//button[@type='submit']")  # Nút đăng ký

        # Xác định các thông báo lỗi
        self.email_invalid_message = (By.XPATH, "//div[text()='\"email\" must be a valid email']")
        self.email_exists_message = (By.XPATH, "//div[text()='Email already exists']")
        self.password_weak_message = (By.XPATH, "//div[text()='Password is too weak']")
        self.password_mismatch_message = (By.XPATH, "//div[text()='Passwords do not match']")
        self.blank_email = (By.XPATH, "//input[@name='email' and @aria-invalid='true']")
        self.blank_password = (By.XPATH, "//input[@name='password' and @aria-invalid='true']")
        self.blank_password_confirm = (By.XPATH, "//input[@name='passwordConfirm' and @aria-invalid='true']")

    # Mở form đăng ký
    def open_register_form(self):
        self.driver.find_element(*self.menu_register).click()

    # Nhập email
    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    # Nhập mật khẩu
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    # Nhập lại mật khẩu
    def enter_password_confirm(self, password_confirm):
        self.driver.find_element(*self.password_confirm_input).send_keys(password_confirm)

    # Nhấn nút đăng ký
    def click_register(self):
        self.driver.find_element(*self.register_button).click()

    # Kiểm tra thông báo lỗi
    def check_error_message(self):
        if self.driver.find_elements(*self.email_invalid_message):
            print("Message: Email is not valid!")
            return "invalid_email"

        if self.driver.find_elements(*self.email_exists_message):
            print("Message: Email already exists!")
            return "email_exists"

        if self.driver.find_elements(*self.password_weak_message):
            print("Message: Password is too weak!")
            return "weak_password"

        if self.driver.find_elements(*self.password_mismatch_message):
            print("Message: Passwords do not match!")
            return "password_mismatch"

        if self.driver.find_elements(*self.blank_email):
            print("Message: Email field is blank!")
            return "chua_nhap_email"

        if self.driver.find_elements(*self.blank_password):
            print("Message: Password field is blank!")
            return "chua_nhap_password"

        if self.driver.find_elements(*self.blank_password_confirm):
            print("Message: Password confirmation field is blank!")
            return "chua_nhap_password_confirm"

        print("No error message appeared.")
        return None
