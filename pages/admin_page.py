from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.create_new_product_page import CreateNewProductPage
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.new_product_link = (By.CSS_SELECTOR, "a[href='/admin/products/new'] button.chakra-button.css-1kc3ghm")  # Nút Add New

    def open_new_product_page(self):
        """Mở trang tạo sản phẩm mới từ navbar."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.new_product_link)
            ).click()
            logging.info("Clicked Add New button")
            return CreateNewProductPage(self.driver)
        except TimeoutException:
            logging.error("❌ Timeout waiting for Add New button")
            raise

    def check_new_product_page_display(self):
        """Kiểm tra trang thêm sản phẩm hiển thị đúng."""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.url_contains("/admin/products/new")
            )
            logging.info("✅ New product page displayed correctly")
            return True
        except TimeoutException:
            logging.error("❌ New product page not displayed")
            return False