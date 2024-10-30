import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SignupTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://e-commerce-for-testing.onrender.com")
        time.sleep(2)

    def test_signup_after_logout(self):
        driver = self.driver
        
        # Nhấn vào nút "Register" để đăng ký
        register_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Register')]")
        register_button.click()
        time.sleep(5)

        # Nhập thông tin đăng ký hợp lệ
        driver.find_element(By.NAME, "username").send_keys("newuser")  # Username input
        driver.find_element(By.NAME, "email").send_keys("newuser@example.com")  # E-mail input
        driver.find_element(By.NAME, "password").send_keys("password123")  # Password input
        driver.find_element(By.NAME, "passwordConfirm").send_keys("password123")  # Password Confirm input
        driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Sign Up button
        time.sleep(5)

        # Kiểm tra thông báo thành công
        try:
            success_message = driver.find_element(By.CLASS_NAME, "success-message")
            self.assertIsNotNone(success_message)
            print("Đăng ký thành công!")
        except Exception as e:
            self.fail(f"Đăng ký không thành công! {str(e)}")

    def test_signup_invalid_username(self):
        driver = self.driver
        
        # Nhấn vào nút "Register" để đăng ký
        register_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Register')]")
        register_button.click()
        time.sleep(5)

        # Nhập thông tin đăng ký không hợp lệ
        driver.find_element(By.NAME, "username").send_keys("")  # Username trống
        driver.find_element(By.NAME, "email").send_keys("newuser@example.com")  # E-mail input hợp lệ
        driver.find_element(By.NAME, "password").send_keys("password123")  # Password input
        driver.find_element(By.NAME, "passwordConfirm").send_keys("password123")  # Password Confirm input
        driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Sign Up button
        time.sleep(5)

        # Kiểm tra thông báo lỗi cho username trống
        try:
            error_message = driver.find_element(By.CLASS_NAME, "error-message")
            self.assertIsNotNone(error_message)
            print("Đăng ký không thành công do tên người dùng trống!")
        except Exception as e:
            self.fail(f"Không thấy thông báo lỗi cho tên người dùng trống! {str(e)}")

    def test_signup_invalid_email(self):
        driver = self.driver
        
        # Nhấn vào nút "Register" để đăng ký
        register_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Register')]")
        register_button.click()
        time.sleep(5)

        # Nhập thông tin đăng ký không hợp lệ
        driver.find_element(By.NAME, "username").send_keys("newuser")  # Username input hợp lệ
        driver.find_element(By.NAME, "email").send_keys("invalidemail")  # E-mail input không hợp lệ
        driver.find_element(By.NAME, "password").send_keys("password123")  # Password input
        driver.find_element(By.NAME, "passwordConfirm").send_keys("password123")  # Password Confirm input
        driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Sign Up button
        time.sleep(5)

        # Kiểm tra thông báo lỗi cho email không hợp lệ
        try:
            error_message = driver.find_element(By.CLASS_NAME, "error-message")
            self.assertIsNotNone(error_message)
            print("Đăng ký không thành công do email không hợp lệ!")
        except Exception as e:
            self.fail(f"Không thấy thông báo lỗi cho email không hợp lệ! {str(e)}")

    def test_signup_password_too_short(self):
        driver = self.driver
        
        # Nhấn vào nút "Register" để đăng ký
        register_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Register')]")
        register_button.click()
        time.sleep(5)

        # Nhập thông tin đăng ký không hợp lệ
        driver.find_element(By.NAME, "username").send_keys("newuser")  # Username input hợp lệ
        driver.find_element(By.NAME, "email").send_keys("newuser@example.com")  # E-mail input hợp lệ
        driver.find_element(By.NAME, "password").send_keys("123")  # Password input quá ngắn
        driver.find_element(By.NAME, "passwordConfirm").send_keys("123")  # Password Confirm input
        driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Sign Up button
        time.sleep(5)

        # Kiểm tra thông báo lỗi cho mật khẩu quá ngắn
        try:
            error_message = driver.find_element(By.CLASS_NAME, "error-message")
            self.assertIsNotNone(error_message)
            print("Đăng ký không thành công do mật khẩu quá ngắn!")
        except Exception as e:
            self.fail(f"Không thấy thông báo lỗi cho mật khẩu quá ngắn! {str(e)}")

    def test_signup_password_mismatch(self):
        driver = self.driver
        
        # Nhấn vào nút "Register" để đăng ký
        register_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Register')]")
        register_button.click()
        time.sleep(5)

        # Nhập thông tin đăng ký không hợp lệ
        driver.find_element(By.NAME, "username").send_keys("newuser")  # Username input hợp lệ
        driver.find_element(By.NAME, "email").send_keys("newuser@example.com")  # E-mail input hợp lệ
        driver.find_element(By.NAME, "password").send_keys("password123")  # Password input
        driver.find_element(By.NAME, "passwordConfirm").send_keys("wrongpassword")  # Password Confirm input không khớp
        driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Sign Up button
        time.sleep(5)

        # Kiểm tra thông báo lỗi cho mật khẩu không khớp
        try:
            error_message = driver.find_element(By.CLASS_NAME, "error-message")
            self.assertIsNotNone(error_message)
            print("Đăng ký không thành công do mật khẩu không khớp!")
        except Exception as e:
            self.fail(f"Không thấy thông báo lỗi cho mật khẩu không khớp! {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
