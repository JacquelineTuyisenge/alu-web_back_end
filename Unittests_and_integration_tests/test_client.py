#!/usr/bin/env python3

'''unittest for GithubOrgClient'''

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    '''Tests for GithubOrgClient'''

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        '''Test that GithubOrgClient.org returns the correct value'''
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)

        result = client.org

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected)

    def test_public_repos_url(self):
        '''Test _public_repos_url property'''
        expected_repos_url = "https://api.github.com/orgs/testorg/repos"

        # Mock the org property to return a known payload
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": expected_repos_url}

            client = GithubOrgClient("testorg")
            result = client._public_repos_url

            self.assertEqual(result, expected_repos_url)

if __name__ == '__main__':
    unittest.main(verbosity=2)
