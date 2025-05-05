from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv

def crawl_vnexpress_science():
    # Cấu hình trình duyệt Chrome chạy ở chế độ không giao diện
    options = Options()
    options.add_argument("--headless")  # Chạy không giao diện
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")

    # Khởi tạo trình điều khiển Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    url = "https://vnexpress.net/khoa-hoc"
    driver.get(url)
    
    try:
        # Chờ trang tải và tìm danh sách bài viết
        wait = WebDriverWait(driver, 10)
        articles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".item-news")))

        # Lưu danh sách bài viết
        article_data = []
        for article in articles:
            try:
                title_element = article.find_element(By.CSS_SELECTOR, ".title-news a")
                title = title_element.text.strip()
                link = title_element.get_attribute("href")

                # Kiểm tra sự tồn tại của mô tả bài viết
                try:
                    description_element = article.find_element(By.CSS_SELECTOR, ".description")
                    description = description_element.text.strip() if description_element else ""
                except Exception as e:
                    description = ""  # Nếu không tìm thấy mô tả, để trống

                article_data.append({"title": title, "link": link, "description": description})
            except Exception as e:
                print(f"Lỗi khi lấy dữ liệu bài viết: {e}")

        driver.quit()

        # Lưu vào file CSV
        csv_filename = "vnexpress_science_articles.csv"
        with open(csv_filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "link", "description"])
            writer.writeheader()
            writer.writerows(article_data)

        print(f"Danh sách bài viết đã được lưu vào {csv_filename}")
        return article_data

    except Exception as e:
        print(f"Lỗi khi thu thập dữ liệu: {e}")
        driver.quit()
        return None

# Gọi hàm để crawl dữ liệu
science_articles = crawl_vnexpress_science()