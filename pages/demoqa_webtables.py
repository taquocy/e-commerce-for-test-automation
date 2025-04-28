from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class webtables:
    def __init__(self, driver):
        self.driver = driver
        
        self.delete1 = (By.XPATH, "//*[@id='delete-record-1']")
        self.delete2 = (By.XPATH, "//*[@id='delete-record-2']")
        self.delete3 = (By.XPATH, "//*[@id='delete-record-3']")

    def click_delete1(self):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.delete1)
        )
        self.driver.find_element(*self.delete1).click()
        
    def click_delete2(self):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.delete2)
        )
        self.driver.find_element(*self.delete2).click()
        
    def click_delete3(self):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.delete3)
        )
        self.driver.find_element(*self.delete3).click()    
    
