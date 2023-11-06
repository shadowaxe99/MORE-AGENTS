
import unittest
from openvas_scanner import OpenvasScanner

class TestOpenvasScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = OpenvasScanner()

    def test_scan(self):
        result = self.scanner.scan('127.0.0.1')
        self.assertIsInstance(result, dict)

    def test_scan_invalid_ip(self):
        with self.assertRaises(ValueError):
            self.scanner.scan('999.999.999.999')

if __name__ == '__main__':
    unittest.main()
