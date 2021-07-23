# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.  # noqa: E501

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AudioAssets(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'album_art': 'AudioAssetDetails',
        'clean_audio': 'AudioAssetDetails',
        'original_audio': 'AudioAssetDetails',
        'preview_mp3': 'AudioAssetDetails',
        'preview_ogg': 'AudioAssetDetails',
        'waveform': 'AudioAssetDetails'
    }

    attribute_map = {
        'album_art': 'album_art',
        'clean_audio': 'clean_audio',
        'original_audio': 'original_audio',
        'preview_mp3': 'preview_mp3',
        'preview_ogg': 'preview_ogg',
        'waveform': 'waveform'
    }

    def __init__(self, album_art=None, clean_audio=None, original_audio=None, preview_mp3=None, preview_ogg=None, waveform=None):  # noqa: E501
        """AudioAssets - a model defined in Swagger"""  # noqa: E501
        self._album_art = None
        self._clean_audio = None
        self._original_audio = None
        self._preview_mp3 = None
        self._preview_ogg = None
        self._waveform = None
        self.discriminator = None
        if album_art is not None:
            self.album_art = album_art
        if clean_audio is not None:
            self.clean_audio = clean_audio
        if original_audio is not None:
            self.original_audio = original_audio
        if preview_mp3 is not None:
            self.preview_mp3 = preview_mp3
        if preview_ogg is not None:
            self.preview_ogg = preview_ogg
        if waveform is not None:
            self.waveform = waveform

    @property
    def album_art(self):
        """Gets the album_art of this AudioAssets.  # noqa: E501


        :return: The album_art of this AudioAssets.  # noqa: E501
        :rtype: AudioAssetDetails
        """
        return self._album_art

    @album_art.setter
    def album_art(self, album_art):
        """Sets the album_art of this AudioAssets.


        :param album_art: The album_art of this AudioAssets.  # noqa: E501
        :type: AudioAssetDetails
        """

        self._album_art = album_art

    @property
    def clean_audio(self):
        """Gets the clean_audio of this AudioAssets.  # noqa: E501


        :return: The clean_audio of this AudioAssets.  # noqa: E501
        :rtype: AudioAssetDetails
        """
        return self._clean_audio

    @clean_audio.setter
    def clean_audio(self, clean_audio):
        """Sets the clean_audio of this AudioAssets.


        :param clean_audio: The clean_audio of this AudioAssets.  # noqa: E501
        :type: AudioAssetDetails
        """

        self._clean_audio = clean_audio

    @property
    def original_audio(self):
        """Gets the original_audio of this AudioAssets.  # noqa: E501


        :return: The original_audio of this AudioAssets.  # noqa: E501
        :rtype: AudioAssetDetails
        """
        return self._original_audio

    @original_audio.setter
    def original_audio(self, original_audio):
        """Sets the original_audio of this AudioAssets.


        :param original_audio: The original_audio of this AudioAssets.  # noqa: E501
        :type: AudioAssetDetails
        """

        self._original_audio = original_audio

    @property
    def preview_mp3(self):
        """Gets the preview_mp3 of this AudioAssets.  # noqa: E501


        :return: The preview_mp3 of this AudioAssets.  # noqa: E501
        :rtype: AudioAssetDetails
        """
        return self._preview_mp3

    @preview_mp3.setter
    def preview_mp3(self, preview_mp3):
        """Sets the preview_mp3 of this AudioAssets.


        :param preview_mp3: The preview_mp3 of this AudioAssets.  # noqa: E501
        :type: AudioAssetDetails
        """

        self._preview_mp3 = preview_mp3

    @property
    def preview_ogg(self):
        """Gets the preview_ogg of this AudioAssets.  # noqa: E501


        :return: The preview_ogg of this AudioAssets.  # noqa: E501
        :rtype: AudioAssetDetails
        """
        return self._preview_ogg

    @preview_ogg.setter
    def preview_ogg(self, preview_ogg):
        """Sets the preview_ogg of this AudioAssets.


        :param preview_ogg: The preview_ogg of this AudioAssets.  # noqa: E501
        :type: AudioAssetDetails
        """

        self._preview_ogg = preview_ogg

    @property
    def waveform(self):
        """Gets the waveform of this AudioAssets.  # noqa: E501


        :return: The waveform of this AudioAssets.  # noqa: E501
        :rtype: AudioAssetDetails
        """
        return self._waveform

    @waveform.setter
    def waveform(self, waveform):
        """Sets the waveform of this AudioAssets.


        :param waveform: The waveform of this AudioAssets.  # noqa: E501
        :type: AudioAssetDetails
        """

        self._waveform = waveform

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AudioAssets, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AudioAssets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
