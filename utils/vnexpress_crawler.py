import csv
import json
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class VnExpressCrawler:
    def __init__(self, headless=True, max_clicks=3, wait_time=10):
        self.headless = headless
        self.max_clicks = max_clicks
        self.wait_time = wait_time
        self.driver = None
        self._init_browser()

    def _init_browser(self):
        options = Options()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, self.wait_time)

    def crawl(self, url):
        print(f"🚀 Crawling: {url}")
        self.driver.get(url)

        # Mở rộng thêm bài viết bằng cách click nút "Xem thêm"
        for _ in range(self.max_clicks):
            try:
                load_more_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-readmore")))
                self.driver.execute_script("arguments[0].click();", load_more_btn)
                time.sleep(2)
            except:
                break  # Không còn nút hoặc hết bài

        try:
            articles = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".item-news")))
        except:
            print("⚠️ Không tìm thấy bài viết.")
            return []

        results = []
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for article in articles:
            try:
                title_element = article.find_element(By.CSS_SELECTOR, ".title-news a")
                title = title_element.text.strip()
                link = title_element.get_attribute("href")

                description_element = article.find_element(By.CSS_SELECTOR, ".description")
                description = description_element.text.strip() if description_element else ""

                results.append({
                    "title": title,
                    "link": link,
                    "description": description,
                    "crawled_at": timestamp
                })
            except Exception as e:
                print(f"❌ Lỗi khi xử lý bài viết: {e}")

        print(f"✅ Đã thu thập {len(results)} bài viết.")
        return results

    def save_to_csv(self, data, filename="articles.csv"):
        if not data:
            print("⚠️ Không có dữ liệu để lưu.")
            return

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"📁 Dữ liệu đã lưu vào {filename}")

    def save_to_json(self, data, filename="articles.json"):
        if not data:
            print("⚠️ Không có dữ liệu để lưu.")
            return

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"📁 Dữ liệu đã lưu vào {filename}")

    def close(self):
        if self.driver:
            self.driver.quit()
            print("🧹 Đã đóng trình duyệt.")


# Ví dụ sử dụng
if __name__ == "__main__":
    crawler = VnExpressCrawler(headless=True)
    articles = crawler.crawl("https://vnexpress.net/suc-khoe")
    crawler.save_to_csv(articles, "vnexpress_health.csv")
    crawler.save_to_json(articles, "vnexpress_health.json")
    crawler.close()
