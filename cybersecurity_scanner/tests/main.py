
import unittest
from openvas_scanner import OpenvasScanner
from sslscan_scanner import SSLScanScanner
from function_app import FunctionApp

class TestMain(unittest.TestCase):

    def setUp(self):
        self.openvas_scanner = OpenvasScanner()
        self.sslscan_scanner = SSLScanScanner()
        self.function_app = FunctionApp()

    def test_openvas_scanner(self):
        result = self.openvas_scanner.scan()
        self.assertIsNotNone(result)

    def test_sslscan_scanner(self):
        result = self.sslscan_scanner.scan()
        self.assertIsNotNone(result)

    def test_function_app(self):
        result = self.function_app.run()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
