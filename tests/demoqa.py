from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

# Mở trang đích
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()

# Lưu handle tab hiện tại
main_window = driver.current_window_handle

# Click vào nút "New Tab"
driver.find_element(By.ID, "tabButton").click()
time.sleep(2)  # Chờ tab mới mở

# Lấy tất cả window handles
all_windows = driver.window_handles

# Duyệt qua các window handle để tìm tab mới
for handle in all_windows:
    if handle != main_window:
        driver.switch_to.window(handle)
        break

# In nội dung trong tab mới
content = driver.find_element(By.ID, "sampleHeading").text
print("Nội dung tab mới:", content)

# Đóng tab mới
driver.close()

# Quay lại tab chính
driver.switch_to.window(main_window)

# Đóng trình duyệt sau 2 giây
time.sleep(2)
driver.quit()
