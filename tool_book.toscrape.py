import requests
from bs4 import BeautifulSoup

# URL của trang cần crawl
url = 'https://books.toscrape.com/'

# Gửi yêu cầu GET tới trang web
response = requests.get(url)

# Kiểm tra nếu kết nối thành công
if response.status_code == 200:
    print("Đã kết nối thành công với trang web!")

    # Phân tích nội dung HTML của trang
    soup = BeautifulSoup(response.text, 'html.parser')

    # Tìm tất cả các sách (giả sử các sách nằm trong các thẻ <article> với class="product_pod")
    books = soup.find_all('article', class_='product_pod')

    # Lấy tên sách và giá
    all_books = []
    for i, book in enumerate(books, 1):
        title = book.find('h3').find('a')['title']  # Tên sách
        price = book.find('p', class_='price_color').text  # Giá sách
        all_books.append((title, price))

    # In ra tất cả các cuốn sách và giá
    print(f"Đã thu thập {len(all_books)} cuốn sách:")
    for book in all_books:
        print(f"{book[0]} - {book[1]}")
else:
    print(f"Lỗi kết nối: {response.status_code}")