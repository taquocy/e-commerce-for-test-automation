from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class elements_textbox:
    def __init__(self, driver):
        self.driver = driver

    self.add_submit = (By.XPATH, "//button[@id='submit']")
    self.add_username = (By.XPATH, "//input[@id='userName']")
    self.add_email = (By.XPATH, "//input[@id='userEmail']")

    def set_username(self, username):
        """Nhập username nếu không trống, nếu trống báo lỗi"""
        if not username.strip():
            raise ValueError(" Username không được bỏ trống!")

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.add_username))
        username_field = self.driver.find_element(*self.add_username)
        username_field.clear()
        username_field.send_keys(username)
        print(f" Đã nhập Username: {username}")

    def set_email(self, email):
        """Nhập email nếu đúng định dạng @gmail.com, nếu sai báo lỗi"""
        if not email.strip():
            raise ValueError(" Email không được bỏ trống!")
        if not email.endswith("@gmail.com"):
            raise ValueError(" Email phải có đuôi @gmail.com!")

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.add_email))
        email_field = self.driver.find_element(*self.add_email)
        email_field.clear()
        email_field.send_keys(email)
        print(f" Đã nhập Email: {email}")

    def click_submit(self):
        """Chỉ nhấn Submit nếu username và email hợp lệ"""
        username_value = self.driver.find_element(*self.add_username).get_attribute("value")
        email_value = self.driver.find_element(*self.add_email).get_attribute("value")

        if not username_value.strip():
            raise ValueError(" Không thể nhấn Submit vì Username bị bỏ trống!")
        if not email_value.strip() or not email_value.endswith("@gmail.com"):
            raise ValueError(" Không thể nhấn Submit vì Email không hợp lệ!")

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_submit))
        submit_button = self.driver.find_element(*self.add_submit)
        submit_button.click()
        print(" Nhấn Submit thành công!")

