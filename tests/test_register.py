import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.register_page import RegisterPage

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://e-commerce-for-testing.onrender.com/")
    yield driver
    driver.quit()

def test_register_user(setup):
    driver = setup
    register_page = RegisterPage(driver)

    register_page.enterEmailField("superadmin@gmail.com")
    register_page.enterPasswordField("admin123")
    register_page.clickRegisterButton()

    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'đăng ký thành công')]"))
        )
        assert success_message.is_displayed()
        print("Đăng ký thành công")
    except TimeoutException:
        print("Đăng ký thất bại: Không tìm thấy thông báo thành công")
        assert False
