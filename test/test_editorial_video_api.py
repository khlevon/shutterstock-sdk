# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.  # noqa: E501

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import shutterstock_sdk
from shutterstock_sdk.api.editorial_video_api import EditorialVideoApi  # noqa: E501
from shutterstock_sdk.rest import ApiException


class TestEditorialVideoApi(unittest.TestCase):
    """EditorialVideoApi unit test stubs"""

    def setUp(self):
        self.api = EditorialVideoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_editorial_video(self):
        """Test case for get_editorial_video

        Get editorial video content details  # noqa: E501
        """
        pass

    def test_get_editorial_video_license_list(self):
        """Test case for get_editorial_video_license_list

        List editorial video licenses  # noqa: E501
        """
        pass

    def test_license_editorial_video(self):
        """Test case for license_editorial_video

        License editorial video content  # noqa: E501
        """
        pass

    def test_list_editorial_video_categories(self):
        """Test case for list_editorial_video_categories

        List editorial video categories  # noqa: E501
        """
        pass

    def test_search_editorial_videos(self):
        """Test case for search_editorial_videos

        Search editorial video content  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
