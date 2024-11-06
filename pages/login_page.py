from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang login
        self.menu_login =  (By.XPATH, "//a[@href='/signin']/button")
        self.username_input = (By.NAME, "email")  # Tìm trường username
        self.password_input = (By.NAME, "password")  # Tìm trường password
        self.login_button = (By.XPATH, "//button[@type='submit']")  # Nút submit
        self.register_button = (By.XPATH, "//button[@type='submit']")  # Nút submit
        self.password_input = (By.NAME, "password")  # Nhap mat khau password
        self.menu_login = (By.XPATH, "//a[@href='/signin']/button")  # Mở form đăng nhập
        self.username_input = (By.NAME, "email")  # Tìm trường email
        self.password_input = (By.NAME, "password")  # Tìm trường mật khẩu
        self.login_button = (By.XPATH, "//button[@type='submit']")  # Nút đăng nhập
        self.register_button = (By.XPATH, "//a[@href='/register']/button")  # Nút đăng ký


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
    # Mở form đăng nhập
    def open_login_form(self):
        self.driver.find_element(*self.menu_login).click()

    # Nhập email (tên đăng nhập)
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    # Nhập mật khẩu
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    # Nhấn nút đăng nhập
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    # Mở trang đăng ký
    def open_register_page(self):
        self.driver.find_element(*self.register_button).click()
