#!/usr/bin/env python3
"""Test client"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock


from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrg"""

    @parameterized.expand([
        ("google", {"org", "Google"}),
        ("abc", {"org": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, mock_get):
        """Test org"""
        mock_get.return_value = expected
        client = GithubOrgClient(org)
        self.assertEqual(client.org, expected)
        mock_get.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(org)
            )

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

    @patch("client.get_json")
    def test_public_repos(self, mock_get):
        """Test public repos"""
        mock_get.return_value = [{"name": "google"}, {"name": "abc"}]
        with patch(
              "client.GithubOrgClient._public_repos_url",
              new_callable=PropertyMock
              ) as mock_org:
            mock_org.return_value = "https://api.github.com/orgs/google"
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), ["google", "abc"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, key, expected):
        """Test for has license"""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, key), expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test Integration of Github org client"""
    @classmethod
    def setUpClass(cls):
        """Set up method"""
        payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload
        }

        def get_payload(url):
            return Mock(**{'json.return_value': payload[url]})

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self):
        """Test public repos without licence"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self):
        """Test public repos licence"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls):
        """Tear down method"""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
