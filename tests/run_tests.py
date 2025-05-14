import unittest
import HtmlTestRunner
import os

# Discover all test cases in the 'tests' folder (relative path)
test_dir = os.path.join(os.path.dirname(__file__), 'tests')
loader = unittest.TestLoader()
suite = loader.discover(test_dir)

# Ensure reports directory exists
reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
os.makedirs(reports_dir, exist_ok=True)

# Run the tests with HtmlTestRunner
runner = HtmlTestRunner.HTMLTestRunner(output=reports_dir, report_name="TestReport", report_title="Automation Test Report")
runner.run(suite)
