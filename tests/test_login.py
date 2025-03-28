import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://yourwebsite.com")  # Thay thế bằng URL trang login thực tế
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_success(driver):
    login_page = LoginPage(driver)
    
    # Mở form đăng nhập
    login_page.open_login_form()
    time.sleep(2)  # Đợi trang tải
    
    # Nhập thông tin đăng nhập hợp lệ
    login_page.enter_username("trongduc@gmail.com")
    login_page.enter_password("duc1234")
    
    # Nhấn nút đăng nhập
    login_page.click_login()
    time.sleep(3)  # Chờ phản hồi từ server
    
    # Xác nhận đăng nhập thành công
    assert "dashboard" in driver.current_url.lower(), "Đăng nhập không thành công!"

def test_login_invalid_password(driver):
    login_page = LoginPage(driver)
    
    # Mở form đăng nhập
    login_page.open_login_form()
    time.sleep(2)
    
    # Nhập thông tin với mật khẩu sai
    login_page.enter_username("trongduc@gmail.com")
    login_page.enter_password("wrongpassword")
    
    # Nhấn nút đăng nhập
    login_page.click_login()
    time.sleep(3)
    
    # Xác nhận có thông báo lỗi
    error_message = driver.find_element(By.CLASS_NAME, "error-message").text
    assert "Invalid credentials" in error_message, "Thông báo lỗi không hiển thị đúng!"

def test_login_empty_fields(driver):
    login_page = LoginPage(driver)
    
    # Mở form đăng nhập
    login_page.open_login_form()
    time.sleep(2)
    
    # Không nhập thông tin
    login_page.click_login()
    time.sleep(3)
    
    # Xác nhận có thông báo lỗi
    error_message = driver.find_element(By.CLASS_NAME, "error-message").text
    assert "Please fill out this field" in error_message, "Thông báo lỗi không hiển thị đúng khi để trống!"

def test_login_valid_user(driver):
    login_page = LoginPage(driver)
    
    # Mở form đăng nhập
    login_page.open_login_form()
    time.sleep(2)
    
    # Nhập thông tin đăng nhập hợp lệ
    login_page.enter_username("trongduc@gmail.com")
    login_page.enter_password("duc12345")
    
    # Nhấn nút đăng nhập
    login_page.click_login()
    time.sleep(3)
    
    # Xác nhận đăng nhập thành công
    assert "dashboard" in driver.current_url.lower(), "Đăng nhập không thành công với tài khoản user hợp lệ!"