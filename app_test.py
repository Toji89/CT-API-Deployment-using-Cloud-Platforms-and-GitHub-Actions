import unittest
from app import app

class TestSumEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Positive test: test sums filtered by a valid result
    def test_get_sums_by_result(self):
        response = self.app.get('/sum/result/4')
        self.assertEqual(response.status_code, 200)

    # Negative test: test sums filtered by an invalid result
    def test_get_sums_by_invalid_result(self):
        response = self.app.get('/sum/result/invalid')
        self.assertEqual(response.status_code, 404)  # Assuming app handles 404 for invalid input

if __name__ == '__main__':
    unittest.main()
