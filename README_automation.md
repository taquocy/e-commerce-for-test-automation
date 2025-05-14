# Hướng dẫn Kiểm thử Tự động Form "Web Tables" trên DemoQA

Tài liệu này cung cấp hướng dẫn về cách chạy script kiểm thử tự động cho chức năng thêm dữ liệu vào bảng "Web Tables" trên trang web [DemoQA](https://demoqa.com/webtables).

## Mục tiêu

* Tự động hóa quy trình thêm một bản ghi mới vào bảng "Web Tables".
* Xác minh rằng dữ liệu đã nhập được hiển thị chính xác trong bảng sau khi thêm.

## Công cụ và Yêu cầu

* **Python 3.x:** Ngôn ngữ lập trình được sử dụng cho script kiểm thử.
* **Selenium WebDriver:** Thư viện Python để tương tác với trình duyệt web.
* **Chrome WebDriver:** Trình điều khiển trình duyệt cho Google Chrome. Đảm bảo bạn đã cài đặt ChromeDriver tương ứng với phiên bản Chrome của mình hoặc script sẽ tự động quản lý việc này thông qua `webdriver_manager`.
* **`webdriver-manager`:** Thư viện Python để tự động quản lý và tải xuống ChromeDriver.
* **`unittest`:** Framework kiểm thử đơn vị tích hợp sẵn trong Python.
* **`configparser`:** Thư viện Python để đọc các file cấu hình.
* **`HtmlTestRunner`:** Thư viện Python để tạo báo cáo kiểm thử HTML.
* **File `config.ini` (tùy chọn):** File cấu hình để lưu trữ các thông tin như URL (trong trường hợp bạn muốn dễ dàng thay đổi URL mục tiêu). Mặc dù script hiện tại đang trực tiếp sử dụng URL của DemoQA.
* **Kết nối Internet:** Cần thiết để tải xuống ChromeDriver (nếu chưa có) và truy cập trang web DemoQA.

## Các bước thực hiện

1.  **Cài đặt các thư viện cần thiết:**

    Mở terminal hoặc command prompt và chạy lệnh sau để cài đặt các thư viện Python cần thiết:

    ```bash
    pip install selenium webdriver-manager html-testrunner configparser
    ```

2.  **Kiểm tra cấu hình (tùy chọn):**

    Nếu bạn có file `config.ini`, hãy đảm bảo nó có cấu trúc tương tự như sau (mặc dù script hiện tại đang sử dụng URL trực tiếp):

    ```ini
    [app]
    login_url = [https://demoqa.com/webtables](https://demoqa.com/webtables)
    ```

3.  **Lưu script Python:**

    Lưu đoạn code Python bạn đã cung cấp (bắt đầu bằng `import unittest`) vào một file có tên, ví dụ: `test_web_tables.py`. Đảm bảo file này nằm trong thư mục dự án của bạn.

4.  **Chạy script kiểm thử:**

    Mở terminal hoặc command prompt, điều hướng đến thư mục chứa file `test_web_tables.py`, và chạy lệnh sau:

    ```bash
    python test_web_tables.py
    ```

    Hoặc để tạo báo cáo HTML:

    ```bash
    python test_web_tables.py -v
    ```

    Lệnh này sẽ chạy test case `test_enter_data_sucescssully`.

5.  **Xem báo cáo kiểm thử (nếu sử dụng `HtmlTestRunner`):**

    Sau khi script chạy xong, một thư mục có tên `reports` sẽ được tạo (nếu chưa có) và chứa file báo cáo HTML (thường có tên mặc định là `report.html`). Mở file này bằng trình duyệt web để xem kết quả kiểm thử chi tiết.

## Giải thích script

Script Python này thực hiện các bước sau:

* **`setUp()`:**
    * Đọc thông tin cấu hình từ file `config.ini` (nếu có).
    * Khởi tạo trình duyệt Chrome bằng cách sử dụng `BrowserSetup.get_driver()` (giả sử class này được định nghĩa ở một nơi khác để quản lý việc khởi tạo trình duyệt).
    * Truy cập trang web DemoQA tại URL `https://demoqa.com/webtables`.

* **`test_enter_data_sucescssully()`:**
    * **Bước 1:** Tìm và nhấp vào nút "Add" để mở form thêm bản ghi mới.
    * **Bước 2:** Tìm và nhập giá trị "Hoang" vào trường "First Name".
    * **Bước 3:** Tìm và nhập giá trị "Tran" vào trường "Last Name".
    * **Bước 4:** Tìm và nhập giá trị "hoang104094@donga.edu.vn" vào trường "Email".
    * **Bước 5:** Tìm và nhập giá trị "20" vào trường "Age".
    * **Bước 6:** Tìm và nhập giá trị "20000000" vào trường "Salary".
    * **Bước 7:** Tìm và nhập giá trị "IT" vào trường "Department".
    * **Bước 8:** Tìm và nhấp vào nút "Submit" để lưu bản ghi.
    * **Bước 9:** Tìm bảng dữ liệu và kiểm tra xem địa chỉ email "hoang104094@donga.edu.vn" có xuất hiện trong bảng hay không. Nếu không, assertion sẽ thất bại và báo cáo lỗi.

* **`tearDown()`:**
    * Đóng trình duyệt sau khi test case hoàn thành.

* **`if __name__ == "__main__":`:**
    * Đảm bảo rằng các test case chỉ được chạy khi script được thực thi trực tiếp (không phải khi được import như một module).
    * Sử dụng `unittest.main()` với `HtmlTestRunner` để tạo báo cáo HTML trong thư mục `reports`.

## Kết quả mong đợi

* Script chạy mà không có lỗi.
* Một bản ghi mới với thông tin đã nhập ("Hoang", "Tran", "hoang104094@donga.edu.vn", "20", "20000000", "IT") được thêm vào bảng trên trang web.
* Báo cáo HTML (nếu được sử dụng) hiển thị kết quả test case là "Passed".

Tài liệu này giúp bạn hiểu cách chạy và diễn giải script kiểm thử tự động cho chức năng thêm dữ liệu vào bảng trên trang DemoQA. Hãy đảm bảo bạn đã cài đặt đúng các công cụ cần thiết trước khi thực hiện.
