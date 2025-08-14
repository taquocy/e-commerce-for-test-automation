from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class elements_textbox:
    def __init__(self, driver):
        self.driver = driver

    self.add_info_textbox = (By.XPATH, '//*[@id="userName-label"]')
    self.add_userEmail = (By.XPATH, '//*[@id="userEmail"]')
    self.add_Submit = (By.XPATH, "//button[text() = 'Submit']")


