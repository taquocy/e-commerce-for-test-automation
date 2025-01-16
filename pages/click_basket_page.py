from selenium.webdriver.common.by import By

class ClickBasketPage:
    def __init__(self, driver):
        self.driver = driver

        self.add_to_basket_button = (By.XPATH, "//button[contains(text(), 'Add to Basket')]")  # Nút thêm vào giỏ
        self.button_home = (By.XPATH, "//a[contains(text(), 'eCommerce')]")  # Nút về trang chủ
        self.button_profile = (By.XPATH, "//a[@href='/profile']")  # Nút chuyển tới trang profile

    def open_home(self):
        self.driver.find_element(*self.button_home).click()

    def click_add_to_basket(self):
        self.driver.find_element(*self.add_to_basket_button).click()

    def is_profile(self):
        button_profile = self.driver.find_element(By.XPATH, "//*[@id='root']/nav//a[3]/button")
        return self.driver.find_element(*self.button_profile).is_displayed()
