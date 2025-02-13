from selenium.webdriver.common.by import By


class ProductDetail:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang product Detail
        self.btn_product_detail = (By.XPATH, "//a[@href='/product/67448abf3b69265c4c3cc327']")
        self.product_img =  (By.XPATH, "//img[@class='image-gallery-image']")
        self.product_name = (By.XPATH, "//h2[@class='chakra-heading css-18j379d']")  # Tìm trường username
        self.product_price = (By.XPATH, "//p[@class='chakra-text css-3kjfdm']")
        self.product_des = (By.XPATH, "//p[@class='chakra-text css-to7kqx']")
        self.product_btnScale = (By.XPATH, "//button[@class='image-gallery-icon image-gallery-fullscreen-button']")
        self.product_btnPlay = (By.XPATH, "//button[@class='image-gallery-icon image-gallery-play-button']")

    def open_product_detail_page(self):
        self.driver.find_element(*self.btn_product_detail).click()

    def load_product_info(self,productImage,productName,productPrice,productDes):
      self.driver.execute_script("arguments[0].src = arguments[1];", self.product_img, productImage)
      self.driver.execute_script("arguments[0].textContent = arguments[1];", self.product_name, productName)   
      self.driver.execute_script("arguments[0].textContent = arguments[1];", self.product_price, productPrice)   
      self.driver.execute_script("arguments[0].textContent = arguments[1];", self.product_des, productDes)  

    def check_btnScale(self, username):
        self.driver.find_element(*self.product_btnScale).click()

    def check_btnPlay(self, username):
        self.driver.find_element(*self.product_btnPlay).click()