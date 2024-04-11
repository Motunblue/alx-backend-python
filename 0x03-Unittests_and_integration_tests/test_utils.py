#!/usr/bin/env python3
"""Test utils"""
import unittest
from parameterized import parameterized

access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Test class for access_nested_map function
    """
    @parameterized.expand([
        ("One nested mappings", {"a": 1}, ("a",), 1),
        ("Two map with one path", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("two maps with two path", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, name, map, path, expected):
        """Test Access nested map"""
        self.assertEqual(access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, map, path):
        """Test if a key error is raised if path not in map"""
        self.assertRaises(KeyError, access_nested_map, map, path)


if __name__ == "__main__":
    unittest.main()
