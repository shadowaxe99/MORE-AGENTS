
import unittest
from cybersecurity_scanner.sslscan_scanner import SSLScanScanner

class TestSSLScanScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = SSLScanScanner()

    def test_scan(self):
        result = self.scanner.scan('www.example.com')
        self.assertIsInstance(result, dict)
        self.assertIn('ssl_certificate', result)

    def test_invalid_url(self):
        with self.assertRaises(ValueError):
            self.scanner.scan('invalid_url')

if __name__ == '__main__':
    unittest.main()
