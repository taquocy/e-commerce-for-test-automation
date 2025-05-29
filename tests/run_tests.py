import unittest
import HtmlTestRunner
import os

# Đặt đường dẫn chính xác đến thư mục tests/
test_dir = os.path.dirname(__file__)  # Trỏ trực tiếp đến thư mục tests/
loader = unittest.TestLoader()
suite = loader.discover(test_dir)

# Đảm bảo thư mục reports/ tồn tại
reports_dir = os.path.join(os.path.dirname(__file__), '../reports')
os.makedirs(reports_dir, exist_ok=True)

# Chạy test với HtmlTestRunner
runner = HtmlTestRunner.HTMLTestRunner(output=reports_dir, report_name="TestReport", report_title="Automation Test Report")
runner.run(suite)