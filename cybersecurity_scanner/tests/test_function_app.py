
import unittest
from azure_functions import function_app

class TestFunctionApp(unittest.TestCase):

    def setUp(self):
        self.app = function_app.FunctionApp()

    def test_process_request(self):
        request = {"threat": "test_threat"}
        response = self.app.process_request(request)
        self.assertEqual(response.status_code, 200)

    def test_process_request_no_threat(self):
        request = {}
        response = self.app.process_request(request)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
