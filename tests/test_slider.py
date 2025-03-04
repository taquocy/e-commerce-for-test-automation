from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class test_slider:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/slider")
        self.driver.maximize_window()
        time.sleep(2)  

    def get_slider_value(self):
        slider_value = self.driver.find_element(By.ID, "sliderValue")
        return slider_value.get_attribute("value")

    def move_slider(self, offset_x):
        slider = self.driver.find_element(By.CLASS_NAME, "range-slider")
        action = ActionChains(self.driver)
        action.click_and_hold(slider).move_by_offset(offset_x, 0).release().perform()
        time.sleep(1)  

    def test_slider(self, expected_value):
        print(f"🔹 Giá trị ban đầu: {self.get_slider_value()}")
        
        self.move_slider(50)

        final_value = self.get_slider_value()
        print(f" Giá trị sau khi kéo: {final_value}")

        if final_value == str(expected_value):
            print(" Test Passed: Giá trị slider đúng!")
        else:
            print(f" Test Failed: Mong đợi {expected_value}, nhưng nhận được {final_value}")

test = test_slider()
test.test_slider(60)
