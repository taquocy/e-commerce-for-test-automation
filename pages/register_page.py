from selenium .webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        # Xác định các phần tử trên trang register

        self.menu_register =  (By.XPATH, "//*[@id=""]/nav/div[2]/a[2]/button")
        self.username_input = (By.NAME, "//*[@id=""]")  # Tìm trường username
        self.password_input = (By.NAME, "//*[@id=""]")  # Tìm trường password
        self.password_input_agian = (By.NAME, "//*[@id=""]") # tìm đường dẫn nhập lại mật khẩu
        self.register_button = (By.XPATH, "//*[@id=""]/div/div/div/div[3]/form/button")  # Nút sign up

    def open_register_form(self):
        self.driver.find_element(*self.menu_register).click()
    # Hàm để nhập tên đăng nhập
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    # Hàm để nhập mật khẩu
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    # Hàm để nhấn nút login
    def click_register(self):
        self.driver.find_element(*self.register_button).click()