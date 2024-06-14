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

        # Mock the org property to return a known payload
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

        # Define the mocked payload and expected result
        mocked_payload = [{"name": "repo1",
                           "license": {"key": "mit"}},
                          {"name": "repo2"}]
        mock_get_json.return_value = mocked_payload
        mock_public_repos_url.return_value = \
            "https://api.github.com/orgs/testorg/repos"

        # Instantiate the client
        client = GithubOrgClient("testorg")

        # Call the method under test
        result = client.public_repos()

        # Define the expected result based on the mocked payload
        expected_repos = ["repo1", "repo2"]

        # Assert that the returned result matches the expected repos
        self.assertEqual(result, expected_repos)

        # Assert that get_json and _public_repos_url were called exactly once
        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()


if __name__ == '__main__':
    unittest.main(verbosity=2)
