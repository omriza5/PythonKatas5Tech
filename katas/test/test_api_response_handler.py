import unittest
from katas.api_response_handler import extract_user_data

class TestExtractUserData(unittest.TestCase):

    def test_valid_response(self):
        api_response = '''
        {
          "users": [
            {
              "id": "1",
              "name": "John Doe",
              "email": "john@example.com",
              "company": {
                "name": "Tech Corp"
              },
              "address": {
                "city": "New York"
              }
            }
          ]
        }
        '''
        expected = [
            {
                "id": "1",
                "name": "John Doe",
                "email": "john@example.com",
                "company_name": "Tech Corp",
                "city": "New York"
            }
        ]
        self.assertEqual(extract_user_data(api_response), expected)

    def test_missing_fields(self):
        api_response = '''
        {
          "users": [
            {
              "id": "2",
              "name": "Jane Smith",
              "email": null,
              "company": null,
              "address": {
                "city": "San Francisco"
              }
            }
          ]
        }
        '''
        expected = [
            {
                "id": "2",
                "name": "Jane Smith",
                "email": None,
                "company_name": None,
                "city": "San Francisco"
            }
        ]
        self.assertEqual(extract_user_data(api_response), expected)

    def test_empty_users_list(self):
        api_response = '''
        {
          "users": []
        }
        '''
        expected = []
        self.assertEqual(extract_user_data(api_response), expected)

    def test_no_users_key(self):
        api_response = '''
        {
          "data": []
        }
        '''
        expected = []
        self.assertEqual(extract_user_data(api_response), expected)

    def test_invalid_json(self):
        api_response = "{ invalid json }"
        with self.assertRaises(ValueError):
            extract_user_data(api_response)

    def test_null_address(self):
        api_response = '''
        {
          "users": [
            {
              "id": "3",
              "name": "Bob Wilson",
              "email": "bob@example.com",
              "company": {
                "name": "Innovation Ltd"
              },
              "address": null
            }
          ]
        }
        '''
        expected = [
            {
                "id": "3",
                "name": "Bob Wilson",
                "email": "bob@example.com",
                "company_name": "Innovation Ltd",
                "city": None
            }
        ]
        self.assertEqual(extract_user_data(api_response), expected)

    def test_no_data(self):
        api_response = "{}"
        expected = []
        self.assertEqual(extract_user_data(api_response), expected)

