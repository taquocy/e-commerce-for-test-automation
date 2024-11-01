from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        # Xác định các phần tử trên trang login
        self.menu_login =  (By.XPATH, "//a[@href='/signin']/button")
        self.email_input = (By.XPATH, "//input[@name='email']")  # Tìm trường username
        self.password_input = (By.XPATH, "//input[@name='password']")  # Tìm trường password
        self.password_confirm_input = (By.XPATH, "//input[@name='passwordConfirm']")  # Tìm trường password
        self.sign_up_button = (By.XPATH, "//button[text()='Sign Up']")  # Nút submit


    # Hàm để nhập tên đăng nhập
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    # Hàm để nhập mật khẩu
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    # Hàm để nhập confirm mật khẩu
    def enter_password(self, password):
        self.driver.find_element(*self.password_confirm_input).send_keys(password)

    # Hàm để nhấn nút login
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
