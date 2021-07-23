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
from swagger_client.api.images_api import ImagesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestImagesApi(unittest.TestCase):
    """ImagesApi unit test stubs"""

    def setUp(self):
        self.api = ImagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_image_collection_items(self):
        """Test case for add_image_collection_items

        Add images to collections  # noqa: E501
        """
        pass

    def test_create_image_collection(self):
        """Test case for create_image_collection

        Create image collections  # noqa: E501
        """
        pass

    def test_delete_image_collection(self):
        """Test case for delete_image_collection

        Delete image collections  # noqa: E501
        """
        pass

    def test_delete_image_collection_items(self):
        """Test case for delete_image_collection_items

        Remove images from collections  # noqa: E501
        """
        pass

    def test_download_image(self):
        """Test case for download_image

        Download images  # noqa: E501
        """
        pass

    def test_get_featured_image_collection(self):
        """Test case for get_featured_image_collection

        Get the details of featured image collections  # noqa: E501
        """
        pass

    def test_get_featured_image_collection_items(self):
        """Test case for get_featured_image_collection_items

        Get the contents of featured image collections  # noqa: E501
        """
        pass

    def test_get_featured_image_collection_list(self):
        """Test case for get_featured_image_collection_list

        List featured image collections  # noqa: E501
        """
        pass

    def test_get_image(self):
        """Test case for get_image

        Get details about images  # noqa: E501
        """
        pass

    def test_get_image_collection(self):
        """Test case for get_image_collection

        Get the details of image collections  # noqa: E501
        """
        pass

    def test_get_image_collection_items(self):
        """Test case for get_image_collection_items

        Get the contents of image collections  # noqa: E501
        """
        pass

    def test_get_image_collection_list(self):
        """Test case for get_image_collection_list

        List image collections  # noqa: E501
        """
        pass

    def test_get_image_keyword_suggestions(self):
        """Test case for get_image_keyword_suggestions

        Get keywords from text  # noqa: E501
        """
        pass

    def test_get_image_license_list(self):
        """Test case for get_image_license_list

        List image licenses  # noqa: E501
        """
        pass

    def test_get_image_list(self):
        """Test case for get_image_list

        List images  # noqa: E501
        """
        pass

    def test_get_image_recommendations(self):
        """Test case for get_image_recommendations

        List recommended images  # noqa: E501
        """
        pass

    def test_get_image_suggestions(self):
        """Test case for get_image_suggestions

        Get suggestions for a search term  # noqa: E501
        """
        pass

    def test_get_similar_images(self):
        """Test case for get_similar_images

        List similar images  # noqa: E501
        """
        pass

    def test_get_updated_images(self):
        """Test case for get_updated_images

        List updated images  # noqa: E501
        """
        pass

    def test_license_images(self):
        """Test case for license_images

        License images  # noqa: E501
        """
        pass

    def test_list_image_categories(self):
        """Test case for list_image_categories

        List image categories  # noqa: E501
        """
        pass

    def test_rename_image_collection(self):
        """Test case for rename_image_collection

        Rename image collections  # noqa: E501
        """
        pass

    def test_search_images(self):
        """Test case for search_images

        Search for images  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
