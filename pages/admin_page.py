from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.create_new_product_page import CreateNewProductPage
from pages.profile_page import ProfilePage

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        # Xác định các phần tử trên trang login
        self.menu_admin =  (By.XPATH, "//a[@href='/admin']/button")
        self.new_product_link = (By.XPATH, "//a[@href='/admin/products/new']/button")
        self.new_profile_link = (By.XPATH, "//a[@href='/profile']/button")

    def open_admin_page(self):
        self.driver.find_element(*self.menu_admin).click()
        
        
    def open_new_product_page(self):
        self.driver.find_element(*self.new_product_link).click()
        return CreateNewProductPage(self.driver)

    def open_profile_page(self):
        self.driver.find_element(*self.new_profile_link).click()
        return ProfilePage(self.driver)
    
    def check_admin_page_display(self):
        try:
            # Tìm nút Admin bằng XPath
            admin_button = self.driver.find_element(By.XPATH, "//button[text()='Admin']")

            # Kiểm tra xem nút Admin có tồn tại không
            assert admin_button is not None, "Admin button does not exist!"
            print("Admin button exists!")

        except NoSuchElementException:
            print("Admin button not found!")

