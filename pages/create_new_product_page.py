# Import các module cần thiết từ thư viện Selenium.
from selenium.webdriver.common.by import By  # Cho phép xác định phần tử bằng các phương thức như XPATH, NAME, v.v.
from selenium.webdriver.support.ui import WebDriverWait  # Cho phép đợi sự kiện xảy ra trên trang.
from selenium.webdriver.support import \
    expected_conditions as EC  # Chứa các điều kiện để chờ (như sự xuất hiện của phần tử).
from selenium.common.exceptions import TimeoutException  # Xử lý ngoại lệ khi chờ quá thời gian quy định.


class CreateNewProductPage():
    # Từ khóa "class" khai báo một lớp (class) trong Python. Lớp chứa các thuộc tính và phương thức.

    def __init__(self, driver):
        """
        Hàm khởi tạo (constructor) của lớp.
        Từ khóa "def" dùng để định nghĩa một hàm.

        __init__ là một hàm đặc biệt được gọi khi một đối tượng của lớp được tạo ra.

        Tham số:
            self: Đại diện cho đối tượng hiện tại (instance) của lớp.
                  Đây là từ khóa bắt buộc trong các phương thức của lớp để truy cập các thuộc tính và phương thức của đối tượng.
            driver: Đối tượng WebDriver của Selenium, được dùng để tương tác với trình duyệt.
        """
        self.driver = driver  # "self.driver": Thuộc tính của đối tượng lưu trữ WebDriver.

        # Xác định các phần tử trên trang "Create New Product" bằng cách sử dụng tuple gồm loại locator và giá trị locator.
        # Các tuple này sẽ được sử dụng bởi Selenium để tìm kiếm các phần tử HTML.

        # --- Phần tử Title ---
        self.title_label = (By.XPATH, "//label[@for='field-:r2:']")
        #  => Đây là tuple chứa:
        #     - By.XPATH: Cách xác định phần tử bằng XPath.
        #     - "//label[@for='field-:r2:']": Giá trị XPath xác định label cho Title.

        self.title_input = (By.NAME, "title")
        #  => Sử dụng By.NAME để xác định trường nhập liệu có thuộc tính name="title".

        self.title_error = (By.XPATH, "//p[contains(text(), 'title is a required field')]")
        #  => XPath này tìm đoạn <p> chứa thông báo lỗi nếu không nhập Title.

        # --- Phần tử Description ---
        self.description_label = (By.XPATH, "//label[@for='field-:r3:']")
        #  => Label cho Description.

        self.description_input = (By.XPATH, "//textarea[@name='description']")
        #  => Textarea để nhập mô tả sản phẩm.

        # --- Phần tử Price ---
        self.price_label = (By.XPATH, "//label[@for='field-:r4:']")
        #  => Label cho trường Price.

        self.price_input = (By.XPATH, "//input[@name='price']")
        #  => Trường nhập giá sản phẩm.

        # --- Phần tử Photos ---
        self.photos_label = (By.XPATH, "//label[@for='field-:r5:']")
        #  => Label cho phần chọn ảnh.

        self.add_photo_button = (By.XPATH, "//button[text()='Add a Photo']")
        #  => Nút "Add a Photo" để thêm ảnh.

        self.photo_input = (By.XPATH, "//input[@name='photos.0']")
        #  => Input để nhập ảnh (có thể là đường dẫn file).

        # --- Nút Submit và Thông báo ---
        self.add_product_button = (By.XPATH, "//button[@type='submit']")
        #  => Nút "Add Product" dùng để gửi form tạo sản phẩm.

        self.message_create_product_successfully = (By.XPATH, "//span[text()='Add product successfully']")
        #  => Thông báo hiển thị khi sản phẩm được thêm thành công.

    def enter_title(self, title):
        """
        Hàm nhập giá trị vào trường Title.

        Tham số:
            self: Đối tượng hiện tại.
            title: Giá trị tiêu đề cần nhập.

        Cú pháp:
            self.driver.find_element(*self.title_input)
            => Tìm phần tử dựa vào locator (ở đây sử dụng tuple self.title_input).
            .send_keys(title): Gửi các ký tự của title đến phần tử đó.
        """
        self.driver.find_element(*self.title_input).send_keys(title)

    def enter_description(self, description):
        """
        Hàm nhập giá trị vào trường Description.

        Tham số:
            description: Nội dung mô tả cần nhập.
        """
        self.driver.find_element(*self.description_input).send_keys(description)

    def enter_price(self, price):
        """
        Hàm nhập giá trị vào trường Price.

        Tham số:
            price: Giá trị giá cần nhập.
        """
        self.driver.find_element(*self.price_input).send_keys(price)

    def click_add_photo(self):
        """
        Hàm click vào nút "Add a Photo".

        .click(): Phương thức thực hiện hành động click vào phần tử.
        """
        self.driver.find_element(*self.add_photo_button).click()

    def enter_image_url(self, image):
        """
        Hàm nhập đường dẫn ảnh vào trường ảnh.

        Tham số:
            image: Đường dẫn hoặc dữ liệu ảnh cần nhập.

        Các bước:
            1. Click vào phần tử input ảnh.
            2. Gửi đường dẫn của ảnh thông qua send_keys.
        """
        self.driver.find_element(*self.photo_input).click()  # Click vào input để focus
        self.driver.find_element(*self.photo_input).send_keys(image)  # Nhập đường dẫn ảnh

    def click_add_product(self):
        """
        Hàm click vào nút "Add Product" để gửi form.
        """
        self.driver.find_element(*self.add_product_button).click()

    def is_success_message_appeared(self):
        """
        Hàm kiểm tra thông báo "Add product successfully" có xuất hiện không.

        Sử dụng WebDriverWait để chờ tối đa 10 giây cho đến khi phần tử chứa thông báo xuất hiện.

        Nếu xuất hiện: in thông báo thành công và trả về True.
        Nếu không: bắt ngoại lệ TimeoutException, in thông báo lỗi và trả về False.
        """
        try:
            # WebDriverWait: Chờ trong 10 giây cho điều kiện dưới đây thỏa mãn.
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.message_create_product_successfully)
            )
            print("Message 'Add product successfully' appeared!")
            return True
        except TimeoutException:
            print("Message 'Add product successfully' did not appear.")
            return False
