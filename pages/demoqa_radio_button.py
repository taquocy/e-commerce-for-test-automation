from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RadioPage:
    def __init__(self, driver):
        self.driver = driver

        self.yes_radio = (By.XPATH, "//label[@for='yesRadio']")
        self.impressive_radio = (By.XPATH, "//label[@for='impressiveRadio']")
        self.no_radio = (By.ID, "noRadio")
        self.result_text = (By.CLASS_NAME, "text-success")

    def click_yes(self):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.yes_radio)
        ).click()
    
    def click_impressive(self):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.impressive_radio)
        ).click()
    
    def is_no_disabled(self):
        return not self.driver.find_element(*self.no_radio).is_enabled()
    
    def get_selected_text(self):
        return self.driver.find_element(*self.result_text).text
