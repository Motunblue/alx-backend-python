#!/usr/bin/env python3
"""Test utils"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock


access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Test class for access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected):
        """Test Access nested map"""
        self.assertEqual(access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, map, path):
        """Test if a key error is raised if path not in map"""
        self.assertRaises(KeyError, access_nested_map, map, path)


class TestGetJson(unittest.TestCase):
    """Test class Get json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, url, expected_payload, mock_get):
        """Test that output of get_json is exqal to the test payload"""
        attr = {'json.return_value': expected_payload}
        mock_get.return_value = Mock(**attr)
        self.assertEqual(get_json(url), expected_payload)
        mock_get.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Test Class for Memoize"""
    def test_memoize(self) -> None:
        """Test memoize"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method") as mock_prop:
            c = TestClass()
            c.a_property()
            c.a_property()
            mock_prop.assert_called_once()


if __name__ == "__main__":
    unittest.main()
