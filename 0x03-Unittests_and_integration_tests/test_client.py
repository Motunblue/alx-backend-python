#!/usr/bin/env python3
"""Test client"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock


from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrg"""

    @parameterized.expand([
        ("google", {"org", "Google"}),
        ("abc", {"org": "abc"})
    ])
    @patch('requests.get')
    def test_org(self, org, expected, mock_get):
        """Test org"""
        attr = {'json.return_value': expected}
        mock_get.return_value = Mock(**attr)
        client = GithubOrgClient(org)
        self.assertEqual(client.org, expected)

    def test_public_repos_url(self):
        """Test public repos url"""
        with patch(
              "client.GithubOrgClient.org",
              new_callable=PropertyMock
              ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google"
                }
            repos_url = GithubOrgClient("google")._public_repos_url
            self.assertEqual(repos_url, "https://api.github.com/orgs/google")


if __name__ == "__main__":
    unittest.main()
