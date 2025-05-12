import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SignupTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/signup")
    
    def test_signup_page_loads(self):
        """Kiểm tra trang đăng ký có hiển thị đúng không"""
        self.assertIn("Sign Up", self.driver.title)
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "form"))
    
    def test_empty_fields_validation(self):
        """Kiểm tra validate khi bỏ trống các trường bắt buộc"""
        driver = self.driver
        submit_button = driver.find_element(By.XPATH, "//button[text()='Sign Up']")
        submit_button.click()
        
        email_error = driver.find_element(By.XPATH, "//input[@name='email']/following-sibling::span")
        password_error = driver.find_element(By.XPATH, "//input[@name='password']/following-sibling::span")
        
        self.assertEqual(email_error.text, "Email là bắt buộc")
        self.assertEqual(password_error.text, "Mật khẩu là bắt buộc")
    
    def test_invalid_email(self):
        """Kiểm tra validate email không hợp lệ"""
        driver = self.driver
        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys("invalid-email")
        email_input.send_keys(Keys.TAB)
        
        email_error = driver.find_element(By.XPATH, "//input[@name='email']/following-sibling::span")
        self.assertEqual(email_error.text, "Email không hợp lệ")
    
    def test_password_mismatch(self):
        """Kiểm tra xác nhận mật khẩu không khớp"""
        driver = self.driver
        password_input = driver.find_element(By.NAME, "password")
        confirm_password_input = driver.find_element(By.NAME, "confirm_password")
        
        password_input.send_keys("password123")
        confirm_password_input.send_keys("password321")
        confirm_password_input.send_keys(Keys.TAB)
        
        mismatch_error = driver.find_element(By.XPATH, "//input[@name='confirm_password']/following-sibling::span")
        self.assertEqual(mismatch_error.text, "Mật khẩu xác nhận không khớp")
    
    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main()
