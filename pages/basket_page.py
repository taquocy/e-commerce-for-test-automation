from selenium.webdriver.common.by import By

class BasketPage:
    def __init__(self, driver):
        self.driver = driver


        self.remove_button = (By.XPATH, "//*[@id='content']/div//button")  
        self.basket_button = (By.XPATH, "//*[@id='root']/nav/div[2]/a[1]/button")  
        self.profile_button = (By.XPATH, "//*[@id='root']/nav/div[2]/a[2]/button")  
        self.item_image = (By.XPATH, "//*[@id='content']/div//a/img")  
        self.total_price = (By.XPATH, "//*[@id='content']/div/span") 


    def remove_item_from_basket(self):
        self.driver.find_element(*self.remove_button).click()



    def open_basket(self):
        self.driver.find_element(*self.basket_button).click()


    def open_profile(self):
        self.driver.find_element(*self.profile_button).click()


    def get_item_image_src(self):
        return self.driver.find_element(*self.item_image).get_attribute("src")


    def get_total_price(self):
        return self.driver.find_element(*self.total_price).text
