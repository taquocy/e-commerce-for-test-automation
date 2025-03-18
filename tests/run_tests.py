import unittest
import HtmlTestRunner

# Discover all test cases in the 'tests' folder
loader = unittest.TestLoader()
suite = loader.discover('tests')  # Assuming your tests are in the 'tests' folder

# Run the tests with HtmlTestRunner
runner = HtmlTestRunner.HTMLTestRunner(output='reports')
runner.run(suite)
