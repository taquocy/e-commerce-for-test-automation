from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver


        # Xác định các phần tử trên trang login
        self.menu_login =  (By.XPATH, "//a[@href='/signin']/button")
        self.username_input = (By.NAME, "email")  # Tìm trường username
        self.password_input = (By.NAME, "password")  # Tìm trường password
        self.login_button = (By.XPATH, "//button[@type='submit']")  # Nút submit
        self.email_not_found_msg = (By.XPATH,"//*[@id='content']/div/div/div/div[2]/div")

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
    def check_email_error(self):
        try:
            # Chờ đợi tối đa 10 giây cho thông báo "Add product successfully" xuất hiện
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_not_found_msg)
            )
            print("Message 'Error Email Message' appeared!")
            return True
        except TimeoutException:
            print("Message 'Error Email Message' did not appear.")
            return False