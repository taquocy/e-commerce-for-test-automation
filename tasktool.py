from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

try:
    # Bước 1: Truy cập trang chủ Báo Mới
    driver.get("https://baomoi.com/")

    # Chờ trang tải (nếu cần)
    time.sleep(3)

    # Bước 2: Thu thập tiêu đề bài viết và ngày giờ
    articles = driver.find_elements(By.XPATH, "//div[@class='story']")

    # Lưu tiêu đề và ngày giờ vào danh sách
    article_data = []
    for article in articles:
        # Lấy tiêu đề bài viết
        title_element = article.find_element(By.XPATH, ".//h4[@class='bm_L']/a")
        title = title_element.text

        # Lấy ngày giờ đăng bài
        try:
            time_element = article.find_element(By.XPATH, ".//time")
            publish_time = time_element.text
        except:
            publish_time = "Không rõ"

        # Thêm vào danh sách
        article_data.append((title, publish_time))

    # Bước 3: Lưu dữ liệu vào tệp articles_with_time.txt
    with open("articles_with_time.txt", "w", encoding="utf-8") as file:
        for idx, (title, publish_time) in enumerate(article_data, start=1):
            file.write(f"{idx}. {title} - {publish_time}\n")

    print("✅ Đã thu thập và lưu tiêu đề bài viết cùng ngày giờ vào tệp articles_with_time.txt.")

finally:
    # Đóng trình duyệt
    driver.quit()