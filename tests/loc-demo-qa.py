from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Truy cập trang Select Menu
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
time.sleep(2)

# 1. Chọn mục trong "Old Style Select Menu"
old_style_select = Select(driver.find_element(By.ID, "oldSelectMenu"))
old_style_select.select_by_visible_text("Purple")
print("Đã chọn 'Purple' trong Old Style Select Menu")
time.sleep(1)

# 2. Chọn màu trong "Multi Select drop down" (nhiều lựa chọn)
multi_select = driver.find_element(By.XPATH, '//div[contains(@class,"css-1hwfws3")]')
multi_select.click()
time.sleep(1)

# Chọn màu "Green"
green_option = driver.find_element(By.XPATH, '//div[text()="Green"]')
green_option.click()
print("Đã chọn 'Green' trong Multi Select Drop Down")
time.sleep(1)

# Chọn thêm màu "Black"
multi_select.click()
black_option = driver.find_element(By.XPATH, '//div[text()="Black"]')
black_option.click()
print("Đã chọn thêm 'Black' trong Multi Select Drop Down")
time.sleep(1)

# 3. Chọn giá trị trong "Select Value" (Dropdown đầu tiên)
select_value = driver.find_element(By.XPATH, '//div[@id="withOptGroup"]//div[contains(@class,"css-1hwfws3")]')
select_value.click()
time.sleep(1)

group_option = driver.find_element(By.XPATH, '//div[text()="Group 1, Option 2"]')
group_option.click()
print("Đã chọn 'Group 1, Option 2' trong Select Value")
time.sleep(1)

# 4. Chọn trong "Select One" (Dropdown thứ 2)
select_one = driver.find_element(By.XPATH, '//div[@id="selectOne"]//div[contains(@class,"css-1hwfws3")]')
select_one.click()
time.sleep(1)

option_professor = driver.find_element(By.XPATH, '//div[text()="Professor"]')
option_professor.click()
print("Đã chọn 'Professor' trong Select One")
time.sleep(1)

# Hoàn tất
print("Hoàn thành tất cả lựa chọn!")

# Đóng trình duyệt
driver.quit()
