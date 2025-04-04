import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
from selenium.webdriver.common.by import By

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class ST23ATestCaseAuto(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get("https://demoqa.com/automation-practice-form")  # Sử dụng URL từ file config

    def test_enter_data_sucescssully(self):
        #Step1 : Enter firstname = 'Bao'
        txtFirstName = self.driver.find_element(By.XPATH,"//*[@id='firstName']")
        txtFirstName.send_keys("Bao")
        time.sleep(1)
        #Step2 : Enter lastname = 'Cao'
        txtLastName = self.driver.find_element(By.XPATH, "//*[@id='lastName']")
        txtLastName.send_keys("Cao")
        time.sleep(1)
        #Step3 : Enter Email = 'bao105833@donga.edu.vn'
        txtEmail = self.driver.find_element(By.XPATH, "//*[@id='userEmail']")
        txtEmail.send_keys("bao105833@donga.edu.vn")
        # Step4 : Select Gender = 'Male'
        male_radio = self.driver.find_element(By.XPATH, "//input[@id='gender-radio-1']")
        self.driver.execute_script("arguments[0].click();", male_radio)  # Sử dụng JavaScript để click nếu Selenium không click được
        time.sleep(1)
        #step5: Enter Phone Number = '0123456789'
        txtPhone = self.driver.find_element(By.XPATH, "//*[@id='userNumber']")
        txtPhone.send_keys("0123456789")
        time.sleep(1)
        #Step6: Điền Date of Birth
        txtBirth = self.driver.find_element(By.XPATH, "//*[@id='dateOfBirthInput']")
        txtBirth.click()  # Mở date picker
        time.sleep(1)

        # Chọn năm
        yearDropdown = self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']")
        yearDropdown.click()
        yearOption = self.driver.find_element(By.XPATH, "//option[@value='2005']")  # Chọn năm 2005
        yearOption.click()
        time.sleep(1)

        # Chọn tháng
        monthDropdown = self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']")
        monthDropdown.click()
        monthOption = self.driver.find_element(By.XPATH, "//option[@value='8']")  # Tháng 9 (0-11)
        monthOption.click()
        time.sleep(1)

        # Chọn ngày
        dayOption = self.driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='23']")
        dayOption.click()
        time.sleep(2)
        # Step7: Enter Subjects = 'Maths'
        txtSubjects = self.driver.find_element(By.XPATH, "//*[@id='subjectsInput']")
        txtSubjects.send_keys("Maths")
        txtSubjects.send_keys(Keys.RETURN)
        time.sleep(1)
        # Step8 : Select Gender = 'Sports'
        txtHobbies = self.driver.find_element(By.XPATH, "//*[@id='hobbies-checkbox-1']")
        self.driver.execute_script("arguments[0].click();", txtHobbies)
        time.sleep(1)
        #Step9 : Upload Picture
        uploadPicture = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='uploadPicture']"))
        )

        file_path = os.path.abspath(r"C:\Users\dinhb\OneDrive\Đính kèm\Hình ảnh5A-98395C3BC3BB}\Hình ảnh\tong-hop-25-hinh-nen-phong-canh-anime-dep-mat-de-thay-doi-man-hinh-desktop-cua-ban_2.jpg")
        uploadPicture.send_keys(file_path)

        if uploadPicture.get_attribute("value"):
            print("✅ Ảnh đã tải lên thành công!")
        else:
            print("❌ Lỗi tải ảnh!")
        time.sleep(1)
        # Step10: Nhập Current Address
        txtAddress = self.driver.find_element(By.XPATH, "//*[@id='currentAddress']")
        txtAddress.send_keys("11 Đặng Thái Thân, Ngũ Hành Sơn, Đà Nẵng")
        time.sleep(1)
        # Step11: Chọn State
        stateDropdown = self.driver.find_element(By.XPATH, "//*[@id='state']")
        stateDropdown.click()
        time.sleep(1)
        # Chờ và chọn State (ví dụ: NCR)
        stateOption = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='NCR']"))
        )
        stateOption.click()
        time.sleep(1)
        # Step12: Chọn City
        cityDropdown = self.driver.find_element(By.XPATH, "//*[@id='city']")
        cityDropdown.click()

        # Chờ và chọn City (ví dụ: Delhi)
        cityOption = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Delhi']"))
        )
        cityOption.click()
        time.sleep(1)
        
        btnSubmit = self.driver.find_element(By.ID, "submit")
        btnSubmit.click()
        
        table = self.driver.find_element(By.XPATH, "//div[@class='rt-table']")
        assert "leduy@donga.edu.vn" in table.text, "Thêm dữ liệu thất bại!"
        return True


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))