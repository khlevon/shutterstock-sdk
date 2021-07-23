# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.  # noqa: E501

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.contributors_api import ContributorsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestContributorsApi(unittest.TestCase):
    """ContributorsApi unit test stubs"""

    def setUp(self):
        self.api = ContributorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_contributor(self):
        """Test case for get_contributor

        Get details about a single contributor  # noqa: E501
        """
        pass

    def test_get_contributor_collection_items(self):
        """Test case for get_contributor_collection_items

        Get the items in contributors' collections  # noqa: E501
        """
        pass

    def test_get_contributor_collections(self):
        """Test case for get_contributor_collections

        Get details about contributors' collections  # noqa: E501
        """
        pass

    def test_get_contributor_collections_list(self):
        """Test case for get_contributor_collections_list

        List contributors' collections  # noqa: E501
        """
        pass

    def test_get_contributor_list(self):
        """Test case for get_contributor_list

        Get details about multiple contributors  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
