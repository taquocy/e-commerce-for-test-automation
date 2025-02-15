import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from basket_page import BasketPage  # Giả sử class nằm trong file basket_page.py

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Hoặc trình duyệt khác bạn đang sử dụng
    driver.get("http://example.com")  # Thay bằng URL của trang cần test
    yield driver
    driver.quit()

@pytest.fixture
def basket_page(driver):
    return BasketPage(driver)

def test_add_product_to_basket(basket_page):
    basket_page.enter_product_name("Test Product")
    basket_page.enter_product_quantity("2")
    basket_page.click_add_to_basket()
    basket_page.click_view_basket()
    
    items = basket_page.get_basket_items()
    assert any("Test Product" in item for item in items), "Product not found in basket"

def test_checkout_button(basket_page):
    basket_page.click_checkout()
    # Kiểm tra xem có chuyển hướng đúng trang thanh toán không
    assert "checkout" in basket_page.driver.current_url.lower(), "Did not navigate to checkout page"
