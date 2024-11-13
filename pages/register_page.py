from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        self.menu_register = (By.XPATH, "//a[@href='/signup']/button")  # Nút mở form đăng ký
        self.email_input = (By.NAME, "email")  # Trường nhập email
        self.password_input = (By.NAME, "password")  # Trường nhập mật khẩu
        self.confirm_password_input = (By.XPATH, "//*[@id='field-:r2:']")  # Trường nhập xác nhận mật khẩu
        self.register_button = (By.XPATH, "//button[@type='submit']")  # Nút đăng ký
        self.success_message = (By.NAME, "message")

    # Phương thức mở form đăng ký
    def open_register_form(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menu_register)
        ).click()

    # Phương thức nhập email
    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.email_input)
        )
        email_field.clear()  # Xóa nội dung trước đó (nếu có)
        email_field.send_keys(email)

    # Phương thức nhập mật khẩu
    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_input)
        )
        password_field.clear()
        password_field.send_keys(password)

    # Phương thức nhập xác nhận mật khẩu
    def enter_confirm_password(self, confirm_password):
        confirm_password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.confirm_password_input)
        )
        confirm_password_field.clear()
        confirm_password_field.send_keys(confirm_password)

    # Phương thức nhấn nút đăng ký
    def click_register(self):
        register_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.register_button)
        )
        ActionChains(self.driver).move_to_element(register_button).click().perform()

    def check_success_message(self):
        try:
            # Chờ đợi cho đến khi thông báo thành công hiển thị
            success_msg = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.success_message)
            )
            return success_msg.text  # Trả về văn bản của thông báo thành công
        except:
            return None  # Nếu không có thông báo thành công, trả về None
