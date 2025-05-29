import unittest
import HtmlTestRunner
import os

test_dir = os.path.dirname(__file__)  # Thư mục tests/
loader = unittest.TestLoader()
suite = loader.discover(test_dir)

reports_dir = os.path.join(os.path.dirname(__file__), '../reports')
os.makedirs(reports_dir, exist_ok=True)

runner = HtmlTestRunner.HTMLTestRunner(output=reports_dir, report_name="TestReport", report_title="Automation Test Report")
runner.run(suite)