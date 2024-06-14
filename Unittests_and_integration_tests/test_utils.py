#!/usr/bin/env python3

'''unittest'''

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    '''testing utils'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''testing access_nested_map'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''testing access_nested_map for KeyError'''
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        # Verify the exception message is as expected
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")

class TestGetJson(unittest.TestCase):
    '''testing get_json'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        '''get_json with mock'''
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            response = get_json(test_url)

            # Assert the mock was called once with the correct URL
            mock_get.assert_called_once_with(test_url)
            # Assert the response is the expected payload
            self.assertEqual(response, test_payload)

if __name__ == '__main__':
    unittest.main()
