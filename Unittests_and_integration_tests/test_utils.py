#!/usr/bin/env python3

'''unittest'''

import unittest
from parameterized import parameterized
from utils import access_nested_map


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

if __name__ == '__main__':
    unittest.main()
