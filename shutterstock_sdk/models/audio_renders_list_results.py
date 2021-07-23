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

class AudioRendersListResults(object):
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
        'audio_renders': 'list[AudioRenderResult]'
    }

    attribute_map = {
        'audio_renders': 'audio_renders'
    }

    def __init__(self, audio_renders=None):  # noqa: E501
        """AudioRendersListResults - a model defined in Swagger"""  # noqa: E501
        self._audio_renders = None
        self.discriminator = None
        self.audio_renders = audio_renders

    @property
    def audio_renders(self):
        """Gets the audio_renders of this AudioRendersListResults.  # noqa: E501

        Audio render results  # noqa: E501

        :return: The audio_renders of this AudioRendersListResults.  # noqa: E501
        :rtype: list[AudioRenderResult]
        """
        return self._audio_renders

    @audio_renders.setter
    def audio_renders(self, audio_renders):
        """Sets the audio_renders of this AudioRendersListResults.

        Audio render results  # noqa: E501

        :param audio_renders: The audio_renders of this AudioRendersListResults.  # noqa: E501
        :type: list[AudioRenderResult]
        """
        if audio_renders is None:
            raise ValueError("Invalid value for `audio_renders`, must not be `None`")  # noqa: E501

        self._audio_renders = audio_renders

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
        if issubclass(AudioRendersListResults, dict):
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
        if not isinstance(other, AudioRendersListResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other