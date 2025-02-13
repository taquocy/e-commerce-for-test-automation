from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.email_label = (By.XPATH, "//label[text()='Email']")  
        self.password_label = (By.XPATH, "//label[text()='Password']")  
        self.password_input = (By.XPATH, "//input[@name='password']")
        self.update_profile_button = (By.XPATH, "//button[contains(@class, 'update-profile-btn')]")  # Dựa trên class
        self.message_update_profile_successfully = (By.XPATH, "//span[text()='Update Profile successfully']")
        self.error_message_missing_special_characters = (By.XPATH, "//span[text()='Enter additional special characters!']")
        self.error_message_missing_capital_letters_and_special_characters = (By.XPATH, "//span[text()='Enter capital letters and special characters!']")
        self.error_message_password_cannot_be_blank = (By.XPATH, "//span[text()='Password cannot be blank!']")
        self.error_message_enter_capital_letters = (By.XPATH, "//span[text()='Enter capital letters!']")
        self.password_length_error_message = (By.XPATH, "//span[text()='Password must be more than 6 characters!']")

    def enter_email(self, email):
        """Nhập địa chỉ email vào trường email."""
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        """Nhập mật khẩu vào trường password."""
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_update_profile(self):
        """Nhấp vào nút cập nhật hồ sơ."""
        self.driver.find_element(*self.update_profile_button).click()

    def is_message_appeared(self, message, xpath):
        """
        Kiểm tra xem một thông báo cụ thể có xuất hiện không.

        Args:
            message (str): Thông báo cần kiểm tra.
            xpath (tuple): XPATH của thông báo.

        Returns:
            bool: True nếu thông báo xuất hiện, False nếu không.
        """
        try:
            # Chờ đợi tối đa 3 giây cho thông báo xuất hiện
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(xpath)
            )
            print(f"Message '{message}' appeared!")
            return True
        except TimeoutException:
            print(f"Message '{message}' did not appear.")
            return False
