from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang login
        self.menu_login = (By.XPATH, "//a[@href='/signin']/button")
        self.username_input = (By.NAME, "email")  # Tìm trường username
        self.password_input = (By.NAME, "password")  # Tìm trường password
        self.login_button = (By.XPATH, "//button[@type='submit']")  # Nút submit
        self.register_button = (By.XPATH, "//button[text()='Register']")  # Nút register
        self.product_link = (By.XPATH, "//a[text()='Products']")  # Liên kết "Products"
        self.ecommerce_link = (By.XPATH, "//a[text()='eCommerce']")  # Liên kết "eCommerce"

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

    # Hàm để nhấn nút register
    def click_register(self):
        self.driver.find_element(*self.register_button).click()
    
    # Hàm để nhấn vào liên kết "Products"
    def click_product_link(self):
        self.driver.find_element(*self.product_link).click()

    # Hàm để nhấn vào liên kết "eCommerce"
    def click_ecommerce_link(self):
        self.driver.find_element(*self.ecommerce_link).click()
