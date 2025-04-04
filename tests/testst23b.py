import unittest
import configparser

import HtmlTestRunner
import sys
import os
import time

# Thêm đường dẫn đến thư mục gốc vào sys.path
from selenium.webdriver.common.by import By

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


class ST23BTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get("https://demoqa.com/automation-practice-form")

    def test_can_add_valid_data_to_form(self):
        #Step1: Điền First Name
        txtFirstName = self.driver.find_element(By.XPATH,"//input[@id='firstName']")
        txtFirstName.send_keys("Huỳnh Phước")
        time.sleep(2)

        #Step2: Điền Last Name
        txtLastName = self.driver.find_element(By.XPATH,"//*[@id='lastName']")
        txtLastName.send_keys('Quân')
        time.sleep(2)

        #Step3: Điền Email
        txtEmail = self.driver.find_element(By.XPATH,"//*[@id='userEmail']")
        txtEmail.send_keys('quan105633@donga.edu.vn')
        time.sleep(2)

        #Step4: Chọn Gender
        rbtGender = self.driver.find_element(By.XPATH,"//*[@id='gender-radio-1']")
        self.driver.execute_script("arguments[0].click();", rbtGender)
        time.sleep(2)

        #Step5: Điền Mobile
        txtMobile = self.driver.find_element(By.XPATH,"//*[@id='userNumber']")
        txtMobile.send_keys('0356726513')
        time.sleep(2)

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
        dayOption = self.driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='1']")
        dayOption.click()
        time.sleep(2)


        #Step7: Điền Subjects
        txtSubjects = self.driver.find_element(By.XPATH,"//*[@id='subjectsInput']")
        txtSubjects.send_keys('Maths')
        time.sleep(2)

        #Step8: Chọn Hobbies
        chkSports = self.driver.find_element(By.XPATH,"//*[@id='hobbies-checkbox-1']")
        self.driver.execute_script("arguments[0].click();", chkSports)
        time.sleep(2)

        #Step9: Upload Picture
        fileUpload = self.driver.find_element(By.XPATH,"//*[@id='uploadPicture']")
        fileUpload.send_keys(r"C:\Users\ADMIN\Pictures\Saved Pictures\trai đẹp.jpg")  # Thay đổi đường dẫn phù hợp
        time.sleep(2)

        #Step10: Điền Current Address
        txtAddress = self.driver.find_element(By.XPATH,"//*[@id='currentAddress']")
        txtAddress.send_keys('420 Trần Đại Nghĩa')
        time.sleep(2)

        #Step11: Chọn State
        cboState = self.driver.find_element(By.XPATH,"//*[@id='state']/div")
        cboState.click()
        stateOption = self.driver.find_element(By.XPATH,"//*[contains(text(),'NCR')]")
        stateOption.click()
        time.sleep(2)

        #Step12: Chọn City
        cboCity = self.driver.find_element(By.XPATH,"//*[@id='city']/div")
        cboCity.click()
        cityOption = self.driver.find_element(By.XPATH,"//*[contains(text(),'Delhi')]")
        cityOption.click()
        time.sleep(2)

        #Step13: Click Submit
        btnSubmit = self.driver.find_element(By.XPATH,"//*[@id='submit']")
        btnSubmit.click()
        time.sleep(2)
        
        btnClose = self.driver.find_element(By.XPATH,"//*[@id='closeLargeModal']")
        btnClose.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))