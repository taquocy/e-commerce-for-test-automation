from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang login
        self.menu_login =  (By.XPATH, "//a[@href='/signin']/button")
        self.username_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.password_confirm_input = (By.NAME, "password_confirm")
        self.register_button = (By.XPATH, "//button[@type='submit']")
        self.input = (By.XPATH, '//*[@id="chatInput"]')

    def open_register_form(self):
        self.driver.find_element(*self.menu_login).click()
    # Hàm để nhập tên đăng nhập
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    # Hàm để nhập mật khẩu
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
        
    # Hàm để nhập mật khẩu confirm
    def enter_password_confirm(self, password_confirm):
        self.driver.find_element(*self.password_confirm_input).send_keys(password_confirm)

    # Hàm để nhấn nút login
    def click_register(self):
        self.driver.find_element(*self.register_button).click()
