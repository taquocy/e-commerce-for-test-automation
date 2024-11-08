from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang login
        self.menu_admin =  (By.XPATH, "//button[text()='Admin']")
        self.order = (By.XPATH, "//button[text()='Orders']")

    def open_admin_page(self):
        self.driver.find_element(*self.menu_admin).click()
    def open_order_page(self):
        self.driver.find_element(*self.order).click()

    def check_admin_page_display(self):
        try:
            # Tìm nút Admin bằng XPath
            admin_button = self.driver.find_element(By.XPATH, "//button[text()='Admin']")

            # Kiểm tra xem nút Admin có tồn tại không
            assert admin_button is not None, "Admin button does not exist!"
            print("Admin button exists!")

        except NoSuchElementException:
            print("Admin button not found!")

