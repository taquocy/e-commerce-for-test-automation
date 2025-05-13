# Test Automation Practice Form

## 1️ Mục tiêu
- Kiểm thử tự động quá trình điền form "Student Registration Form" trên [DemoQA](https://demoqa.com/automation-practice-form).

## 2Công cụ sử dụng
- Selenium WebDriver (Python)
- Chrome WebDriver

## 3️ **Các bước thực hiện**
###  **Step 1**: Mở trình duyệt và truy cập trang form
###  **Step 2**: Nhập dữ liệu vào các trường bắt buộc
- First Name, Last Name, Email, Mobile, Date of Birth, Subjects, Hobbies, Current Address
- Upload hình ảnh

###  **Step 3**: Click nút **Submit**
- Cuộn xuống để nút Submit hiển thị
- Xóa quảng cáo chặn nút Submit (nếu có)
- Click vào nút **Submit**

###  **Step 4**: Xác nhận form gửi thành công
- Kiểm tra bảng hiển thị thông tin đã nhập

## 4️ **Kết quả mong đợi**
- Form gửi thành công và hiển thị thông tin đã nhập đúng.
- Không bị lỗi **ElementClickInterceptedException**.
