
from selenium import webdriver
from selenium.webdriver.common.by import By

# Khởi tạo trình duyệt
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Chạy trình duyệt ở chế độ không giao diện (tùy chọn)
driver = webdriver.Chrome(options=options)
# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# Mở trang web
driver.get("https://vnexpress.net/khoa-hoc")

# Lấy danh sách tiêu đề bài viết
titles = driver.find_elements(By.CSS_SELECTOR, "h3.title-news a")

# In tiêu đề ra màn hình
print("Danh sách tiêu đề bài viết:")
for title in titles:
    print("-", title.text)

# Đóng trình duyệt
driver.quit()

