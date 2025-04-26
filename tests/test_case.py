from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import time

class PracticeFormTest(unittest.TestCase):

    def setUp(self):
        # Bước 1: Mở trình duyệt Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/automation-practice-form")
        print("Đã truy cập trang Practice Form")

    def test_fill_practice_form(self):
        # Bước 2: Nhập First Name
        first_name_input = self.driver.find_element(By.ID, "firstName")
        first_name_input.send_keys("John")
        print("Đã nhập First Name: John")

        # Bước 3: Nhập Last Name
        last_name_input = self.driver.find_element(By.ID, "lastName")
        last_name_input.send_keys("Doe")
        print("Đã nhập Last Name: Doe")

        # Bước 4: Nhập Email
        email_input = self.driver.find_element(By.ID, "userEmail")
        email_input.send_keys("john.doe@example.com")
        print("Đã nhập Email: john.doe@example.com")

        # Bước 5: Chọn giới tính (Male)
        male_radio = self.driver.find_element(By.XPATH, "//label[text()='Male']")
        male_radio.click()
        print("Đã chọn giới tính: Male")

        # Bước 6: Nhập Mobile Number
        mobile_input = self.driver.find_element(By.ID, "userNumber")
        mobile_input.send_keys("1234567890")
        print("Đã nhập Mobile Number: 1234567890")

        # Bước 7: Chọn Date of Birth (chỉ chọn tháng và năm)
        date_of_birth_input = self.driver.find_element(By.ID, "dateOfBirthInput")
        date_of_birth_input.click()
        month_select = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
        month_select.select_by_visible_text("May")
        year_select = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
        year_select.select_by_visible_text("1990")
        day_select = self.driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--0') and not(contains(@class, 'react-datepicker__day--outside-month'))]")
        day_select.click()
        print("Đã chọn Date of Birth: May 1990")

        # Bước 8: Nhập Subjects
        subjects_input = self.driver.find_element(By.ID, "subjectsInput")
        subjects_input.send_keys("Computer Science")
        subjects_input.send_keys(Keys.RETURN)
        print("Đã nhập Subjects: Computer Science")

        # Bước 9: Chọn Hobbies (Sports)
        sports_checkbox = self.driver.find_element(By.XPATH, "//label[text()='Sports']")
        sports_checkbox.click()
        print("Đã chọn Hobbies: Sports")

        # Bước 10: Upload picture (bỏ qua bước này vì cần file thực tế)
        print("Đã bỏ qua bước Upload picture")

        # Bước 11: Nhập Current Address
        address_textarea = self.driver.find_element(By.ID, "currentAddress")
        address_textarea.send_keys("123 Main Street, Anytown, CA 91234")
        print("Đã nhập Current Address: 123 Main Street, Anytown, CA 91234")

        # Bước 12: Chọn State và City (chỉ chọn State)
        state_dropdown = self.driver.find_element(By.ID, "state")
        state_dropdown.click()
        state_item = self.driver.find_element(By.XPATH, "//div[text()='NCR']")
        state_item.click()
        print("Đã chọn State: NCR")

        # Bước 13: Nhấn nút Submit
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()
        print("Đã nhấn nút Submit")
        time.sleep(2) # Chờ modal hiển thị

        # Bước 14: Assert - Kiểm tra xem modal xác nhận có hiển thị hay không
        success_modal = self.driver.find_element(By.ID, "example-modal-sizes-title-lg")
        self.assertTrue(success_modal.is_displayed(), "Modal xác nhận không hiển thị")
        print("Đã kiểm tra: Modal xác nhận hiển thị thành công")

        # Bước 15: Assert - Kiểm tra xem tên trong modal có đúng không
        submitted_name = self.driver.find_element(By.XPATH, "//td[text()='Student Name']/following-sibling::td")
        self.assertEqual(submitted_name.text, "John Doe", "Tên hiển thị trong modal không đúng")
        print(f"Đã kiểm tra: Tên hiển thị trong modal là '{submitted_name.text}'")

    def tearDown(self):
        # Bước 16: Đóng trình duyệt
        self.driver.quit()
        print("Đã đóng trình duyệt")

if __name__ == "__main__":
    unittest.main()