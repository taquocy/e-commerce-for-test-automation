from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo driver (dùng Chrome)
driver = webdriver.Chrome()  # Đảm bảo bạn đã cài ChromeDriver

# Truy cập trang web
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()

# Lưu lại tab hiện tại
original_window = driver.current_window_handle

# Click nút "New Tab"
new_tab_button = driver.find_element(By.ID, "tabButton")
new_tab_button.click()

# Đợi cho tab mới mở (tối đa 10s)
time.sleep(3)

# Lặp qua các cửa sổ và chuyển sang cái mới
for handle in driver.window_handles:
    if handle != original_window:
        driver.switch_to.window(handle)
        break

# Đợi nội dung trong tab mới tải xong
time.sleep(2)

# Lấy và in nội dung trong tab mới
heading = driver.find_element(By.ID, "sampleHeading").text
print("Nội dung tab mới:", heading)

# Đóng tab mới và quay lại tab cũ
driver.close()
driver.switch_to.window(original_window)

# Đóng trình duyệt
driver.quit()
