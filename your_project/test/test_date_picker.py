import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DatePickerTest(unittest.TestCase):
    
    def setUp(self):
        """Khởi tạo trình duyệt và mở trang Date Picker."""
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/date-picker")
        self.driver.maximize_window()
    
    def test_select_date(self):
        """Kiểm tra việc chọn một ngày cụ thể từ Date Picker."""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        # Mở Date Picker
        date_input = wait.until(EC.element_to_be_clickable((By.ID, "datePickerMonthYearInput")))
        date_input.click()
        time.sleep(2)
        
        # Chọn tháng và năm
        month_dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select")))
        month_dropdown.send_keys("June")
        
        year_dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__year-select")))
        year_dropdown.send_keys("2025")
        
        # Chọn ngày
        day = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='15']")))
        day.click()
        
        # Kiểm tra kết quả
        selected_date = date_input.get_attribute("value")
        print("Ngày được chọn:", selected_date)
        self.assertEqual(selected_date, "06/15/2025")
    
    def tearDown(self):
        """Đóng trình duyệt sau khi hoàn tất kiểm thử."""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
