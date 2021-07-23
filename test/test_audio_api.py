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
from swagger_client.api.audio_api import AudioApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAudioApi(unittest.TestCase):
    """AudioApi unit test stubs"""

    def setUp(self):
        self.api = AudioApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_track_collection_items(self):
        """Test case for add_track_collection_items

        Add audio tracks to collections  # noqa: E501
        """
        pass

    def test_create_track_collection(self):
        """Test case for create_track_collection

        Create audio collections  # noqa: E501
        """
        pass

    def test_delete_track_collection(self):
        """Test case for delete_track_collection

        Delete audio collections  # noqa: E501
        """
        pass

    def test_delete_track_collection_items(self):
        """Test case for delete_track_collection_items

        Remove audio tracks from collections  # noqa: E501
        """
        pass

    def test_download_tracks(self):
        """Test case for download_tracks

        Download audio tracks  # noqa: E501
        """
        pass

    def test_get_track(self):
        """Test case for get_track

        Get details about audio tracks  # noqa: E501
        """
        pass

    def test_get_track_collection(self):
        """Test case for get_track_collection

        Get the details of audio collections  # noqa: E501
        """
        pass

    def test_get_track_collection_items(self):
        """Test case for get_track_collection_items

        Get the contents of audio collections  # noqa: E501
        """
        pass

    def test_get_track_collection_list(self):
        """Test case for get_track_collection_list

        List audio collections  # noqa: E501
        """
        pass

    def test_get_track_license_list(self):
        """Test case for get_track_license_list

        List audio licenses  # noqa: E501
        """
        pass

    def test_get_track_list(self):
        """Test case for get_track_list

        List audio tracks  # noqa: E501
        """
        pass

    def test_license_track(self):
        """Test case for license_track

        License audio tracks  # noqa: E501
        """
        pass

    def test_list_genres(self):
        """Test case for list_genres

        List audio genres  # noqa: E501
        """
        pass

    def test_list_instruments(self):
        """Test case for list_instruments

        List audio instruments  # noqa: E501
        """
        pass

    def test_list_moods(self):
        """Test case for list_moods

        List audio moods  # noqa: E501
        """
        pass

    def test_rename_track_collection(self):
        """Test case for rename_track_collection

        Rename audio collections  # noqa: E501
        """
        pass

    def test_search_tracks(self):
        """Test case for search_tracks

        Search for tracks  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
