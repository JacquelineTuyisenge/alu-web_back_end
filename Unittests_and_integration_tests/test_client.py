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

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected)

    def test_public_repos_url(self):
        '''Test _public_repos_url property'''
        expected_repos_url = "https://api.github.com/orgs/testorg/repos"

        with patch.object(GithubOrgClient,
                          'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": expected_repos_url}

            client = GithubOrgClient("testorg")
            result = client._public_repos_url

            self.assertEqual(result, expected_repos_url)

    @patch('client.get_json')
    @patch.object(GithubOrgClient,
                  '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        '''Test GithubOrgClient.public_repos'''

        mocked_payload = [{"name": "repo1",
                           "license": {"key": "mit"}},
                          {"name": "repo2"}]
        mock_get_json.return_value = mocked_payload
        mock_public_repos_url.return_value = \
            "https://api.github.com/orgs/testorg/repos"

        client = GithubOrgClient("testorg")

        result = client.public_repos()

        expected_repos = ["repo1", "repo2"]

        self.assertEqual(result, expected_repos)

        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    @patch('client.access_nested_map')
    def test_has_license(self, repo, license_key, expected_result, mock_access_nested_map):
        '''Test GithubOrgClient.has_license'''

        mock_access_nested_map.return_value = repo.get('license', {}).get('key')

        client = GithubOrgClient("testorg")

        result = client.has_license(repo, license_key)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
