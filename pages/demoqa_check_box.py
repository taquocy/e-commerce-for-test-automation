from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class check_box:
    def __init__(self, driver):
        self.driver = driver
        
        self.yes = (By.XPATH, "//*[@id='yesRadio']")
        self.impressive = (By.XPATH, "//*[@id='impressiveRadio']")
        self.no = (By.XPATH, "//*[@id='noRadio']")

    def click_yes(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.yes)
        )
        self.driver.find_element(*self.yes).click()
    
    def click_impressive(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.impressive)
        )
        self.driver.find_element(*self.impressive).click()
    
    def click_no(self):
        no_element = self.driver.find_element(*self.no)

        if no_element.is_enabled():
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.no)
            )
            no_element.click()
        else:
            pass

    