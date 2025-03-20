from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt (đảm bảo đã cài ChromeDriver)
driver = webdriver.Chrome()

try:
    # Mở trang web
    url = "https://petshopdanang.com/"
    driver.get(url)

    # Chờ một lúc để trang tải xong (có thể điều chỉnh)
    time.sleep(3)

    # Tìm tất cả danh mục sản phẩm và số lượng sản phẩm trong danh mục đó
    categories = driver.find_elements(By.CSS_SELECTOR, ".product-category.product")

    # Lặp qua từng danh mục để lấy tên và số lượng sản phẩm
    for category in categories:
        title = category.find_element(By.CSS_SELECTOR, ".woocommerce-loop-category__title").text
        print(title)  # In ra tiêu đề danh mục, có thể chứa số lượng sản phẩm

finally:
    # Đóng trình duyệt sau khi hoàn thành
    driver.quit()