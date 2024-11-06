from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver


        # Xác định các phần tử trên trang login
        self.menu_login =  (By.XPATH, "//a[@href='/signin']/button")
        self.menu_register =  (By.XPATH, "//a[@href='/signup']/button")
        self.username_input = (By.NAME, "email")  # Tìm trường username
        self.password_input = (By.NAME, "password")  # Tìm trường password
        self.login_button = (By.XPATH, "//button[@type='submit']")  # Nút submit
        self.title = "//h2[normalize-space(text())='%s']"

    def open_login_form(self):
        self.driver.find_element(*self.menu_login).click()

    def open_register_form(self):
        self.driver.find_element(*self.menu_register).click()

    # Hàm để nhập tên đăng nhập
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    # Hàm để nhập mật khẩu
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    # Hàm để nhấn nút login
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
    def check_profile_page_display(self):
        try:
            # Tìm nút Admin bằng XPath
            admin_button = self.driver.find_element(By.XPATH, "//button[text()='Profile']")

            # Kiểm tra xem nút Admin có tồn tại không
            assert admin_button is not None, "Profile button does not exist!"
            print("Profile button exists!")

        except NoSuchElementException:
            print("Profile button not found!")

    def get_error_message(self):
        # Locate the error message element and return its text
        error_element = self.driver.find_element(By.XPATH, "//*[@class and contains(concat(' ', normalize-space(@class), ' '), ' chakra-alert ')]")  # Replace with actual selector
        return error_element.text
    
    def get_title(self, ttle:str):
        title_locator = (By.XPATH, self.title % ttle)
        title_element = self.driver.find_element(*title_locator)
        return title_element.text
