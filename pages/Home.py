from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang Home
        self.add_to_basket_button = (By.XPATH, "//button[text()='Add to Basket']")
        self.add_to_cart_button = (By.XPATH, "//button[text()='Add to Cart']")
        self.load_more_button = (By.XPATH, "//button[text()='Load More']")