import unittest
import configparser
import time
import sys
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.browser_setup import BrowserSetup
import HtmlTestRunner


class AutoCompletePage(unittest.TestCase):

    def setUp(self):
        """Setup browser and navigate to the Auto Complete page."""
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.driver = BrowserSetup.get_driver()
        self.driver.get("https://demoqa.com/auto-complete")
        self.driver.maximize_window()

    def test_auto_complete_both_inputs(self):
        """Test Auto Complete for both Single and Multiple Color Name inputs."""

        # **Test Single Color Name input**
        single_color_input = self.driver.find_element(By.XPATH, "//input[@id='autoCompleteSingleInput']")
        single_color_input.send_keys("Blue")
        time.sleep(1)  # Wait for suggestions to appear
        single_color_input.send_keys(Keys.ARROW_DOWN)
        single_color_input.send_keys(Keys.ENTER)

        # Verify Single Color Name selection
        selected_single_color = self.driver.find_element(By.XPATH, "//div[contains(@class, 'auto-complete__single-value')]")
        self.assertIn("Blue", selected_single_color.text, "Single Auto Complete did not select the expected color!")

        # **Test Multiple Color Names input**
        multiple_color_input = self.driver.find_element(By.XPATH, "//input[@id='autoCompleteMultipleInput']")
        colors = ["Red", "Green", "Yellow"]

        for color in colors:
            multiple_color_input.send_keys(color)
            time.sleep(1)  # Allow time for suggestions
            multiple_color_input.send_keys(Keys.ARROW_DOWN)
            multiple_color_input.send_keys(Keys.ENTER)

        # Verify Multiple Colors selection
        selected_colors = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'auto-complete__multi-value__label')]")
        selected_texts = [color.text for color in selected_colors]

        for color in colors:
            self.assertIn(color, selected_texts, f"Multiple Auto Complete did not select {color}!")

    def tearDown(self):
        """Close the browser after test execution."""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
