from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định phần tử button "Add to Basket"
        self.add_to_basket_button = (By.XPATH, "//button[contains(text(), 'Add to Basket')]")
        self.button_home = (By.XPATH, "//a[contains(text(), 'eCommerce')]")
        self.button_profile = (By.XPATH, "//*[@id='root']/nav//a[3]/button")

    # Hàm để nhấn vào button "Add to Basket"
    def open_home(self):
        self.driver.find_element(*self.button_home).click()
        
    def click_add_to_basket(self):
        self.driver.find_element(*self.add_to_basket_button).click()
        
    # Hàm kiểm tra xem sản phẩm đã được thêm vào giỏ hàng hay chưa
    def is_profile(self):
        # Ở đây bạn có thể kiểm tra dựa trên sự xuất hiện của một thông báo, icon giỏ hàng, hoặc cập nhật số lượng giỏ hàng
        # Ví dụ:
        button_profile = self.driver.find_element(By.XPATH, "//*[@id='root']/nav//a[3]/button")
        return button_profile.is_displayed()
