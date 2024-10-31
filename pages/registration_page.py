from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang đăng ký
        self.email_input = (By.NAME, "email") 
        self.password_input = (By.NAME, "password")  
        self.passwordConfirm_input = (By.NAME, "passwordConfirm") 
        self.menu_register =  (By.XPATH, "//a[@href='/signup']/button") 
        self.success_message = (By.CLASS_NAME, "success-message") 
        self.error_message = (By.XPATH, "//*[@id='content']/div/div/div/div[2]/div")  
        self.register_button = (By.XPATH, "//button[@type='submit']") 
        self.profile_button = (By.XPATH, "//a[@href='/profile']") 
    # Hàm để nhập email
    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    # Hàm để nhập mật khẩu
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    # Hàm để nhập xác nhận mật khẩu
    def enter_passwordConfirm(self, passwordConfirm):
        self.driver.find_element(*self.passwordConfirm_input).send_keys(passwordConfirm)

    # Hàm để nhấn nút đăng ký
    def click_sign_up(self):
        self.driver.find_element(*self.menu_register).click()

    # Hàm để lấy thông báo lỗi
    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
    
    def get_email_in_use_error_message(self):
        try:
            email_in_use_error_message = self.driver.find_element(By.XPATH, "//div[@data-status='error'][contains(text(), 'This e-mail already using.')]")
            return email_in_use_error_message.text
        except NoSuchElementException:
            return None
    
    def click_register(self):
        self.driver.find_element(*self.register_button).click()

    def is_registration_successful(self):
        try:
            # Kiểm tra xem nút/profile có tồn tại không
            self.driver.find_element(*self.profile_button)
            return True  # Nếu tìm thấy nút, đăng ký thành công
        except NoSuchElementException:
            return False  # Nếu không tìm thấy, đăng ký không thành công