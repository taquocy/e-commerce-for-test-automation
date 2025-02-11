from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang login
        self.menu_login = (By.XPATH, "//a[@href='/signin']/button")
        self.username_input = (By.NAME, "email")  # Tìm trường username
        self.password_input = (By.NAME, "password")  # Tìm trường password
        self.login_button = (By.XPATH, "//button[@type='submit']")  # Nút submit

        # Thêm locator cho thông báo lỗi
        self.email_error = (By.XPATH, "//div[1]/div/div/div/div/div[3]/form/div[1]/div")
        self.password_error = (
            By.XPATH,
            "//div[1]/div/div/div/div/div[3]/form/div[2]/div[2]",
        )

    def open_login_form(self):
        # Thêm thời gian chờ
        wait = WebDriverWait(self.driver, 10)
        menu_login = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/signin']/button"))
        )
        menu_login.click()

    # Hàm để nhập tên đăng nhập
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    # Hàm để nhập mật khẩu
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    # Hàm để nhấn nút login
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        try:
            # Sử dụng locator đã định nghĩa trong __init__
            email_error = self.driver.find_element(*self.email_error).text
            password_error = self.driver.find_element(*self.password_error).text

            error_messages = []
            if email_error:
                error_messages.append(email_error)
            if password_error:
                error_messages.append(password_error)

            return " ".join(error_messages)
        except:
            return ""

    def get_email_error_message(self):
        """Lấy thông báo lỗi của trường email"""
        return self.driver.find_element(
            By.CSS_SELECTOR, "input[type='email'] + div"
        ).text

    def get_password_error_message(self):
        """Lấy thông báo lỗi của trường password"""
        return self.driver.find_element(
            By.CSS_SELECTOR, "input[type='password'] + div"
        ).text
