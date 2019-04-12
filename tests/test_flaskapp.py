import unittest,json

from main import app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_unauthorized(self):
        response = self.app.get('/authorized')
        # Check if the request fails with authorization error
        self.assertEqual(response._status_code, 401, 'Unauthorized access to page without login')

    def test_multiply(self):
        response = self.app.get('/multiply?x=5&y=7')
        resp = json.loads(response.data)
        self.assertEqual(resp['answer'], 35, 'Multiply endpoint failed known answer 7*5 = 35')

    def test_uppercase(self):
        response = self.app.get('/touppercase?s=abc')
        resp = response.data
        self.assertEqual(resp, "ABC", 'Uppercase endpoint failed known answer abc -> ABC')


if __name__ == '__main__':
    unittest.main()
