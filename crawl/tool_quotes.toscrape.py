import requests
from bs4 import BeautifulSoup

# URL của trang cần crawl
url = 'https://quotes.toscrape.com/'

# Gửi yêu cầu GET tới trang web
response = requests.get(url)

# Kiểm tra nếu kết nối thành công
if response.status_code == 200:
    print("Đã kết nối thành công với trang web!")

    # Phân tích nội dung HTML của trang
    soup = BeautifulSoup(response.text, 'html.parser')

    # Tìm tất cả các trích dẫn (giả sử mỗi trích dẫn nằm trong thẻ <div> với class="quote")
    quotes = soup.find_all('div', class_='quote')

    # Lấy trích dẫn, tác giả và chủ đề
    all_quotes = []
    for i, quote in enumerate(quotes, 1):
        text = quote.find('span', class_='text').text  # Trích dẫn
        author = quote.find('small', class_='author').text  # Tác giả
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]  # Chủ đề (tags)

        all_quotes.append((text, author, tags))

    # In ra tất cả các trích dẫn, tác giả và chủ đề
    print(f"Đã thu thập {len(all_quotes)} trích dẫn:")
    for quote in all_quotes:
        print(f"Trích dẫn: {quote[0]}\nTác giả: {quote[1]}\nChủ đề: {', '.join(quote[2])}\n")
else:
    print(f"Lỗi kết nối: {response.status_code}")