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

class LicenseFormat(object):
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
        'description': 'str',
        'format': 'str',
        'media_type': 'str',
        'min_resolution': 'int',
        'size': 'str'
    }

    attribute_map = {
        'description': 'description',
        'format': 'format',
        'media_type': 'media_type',
        'min_resolution': 'min_resolution',
        'size': 'size'
    }

    def __init__(self, description=None, format=None, media_type=None, min_resolution=None, size=None):  # noqa: E501
        """LicenseFormat - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._format = None
        self._media_type = None
        self._min_resolution = None
        self._size = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if format is not None:
            self.format = format
        if media_type is not None:
            self.media_type = media_type
        if min_resolution is not None:
            self.min_resolution = min_resolution
        if size is not None:
            self.size = size

    @property
    def description(self):
        """Gets the description of this LicenseFormat.  # noqa: E501

        Description of the license  # noqa: E501

        :return: The description of this LicenseFormat.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LicenseFormat.

        Description of the license  # noqa: E501

        :param description: The description of this LicenseFormat.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def format(self):
        """Gets the format of this LicenseFormat.  # noqa: E501

        Format or extension of the media, such as mpeg for videos or jpeg for images  # noqa: E501

        :return: The format of this LicenseFormat.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this LicenseFormat.

        Format or extension of the media, such as mpeg for videos or jpeg for images  # noqa: E501

        :param format: The format of this LicenseFormat.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def media_type(self):
        """Gets the media_type of this LicenseFormat.  # noqa: E501

        Media type of the license  # noqa: E501

        :return: The media_type of this LicenseFormat.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this LicenseFormat.

        Media type of the license  # noqa: E501

        :param media_type: The media_type of this LicenseFormat.  # noqa: E501
        :type: str
        """
        allowed_values = ["image", "video", "audio", "editorial"]  # noqa: E501
        if media_type not in allowed_values:
            raise ValueError(
                "Invalid value for `media_type` ({0}), must be one of {1}"  # noqa: E501
                .format(media_type, allowed_values)
            )

        self._media_type = media_type

    @property
    def min_resolution(self):
        """Gets the min_resolution of this LicenseFormat.  # noqa: E501

        Width of the media, in pixels, allowed by this license  # noqa: E501

        :return: The min_resolution of this LicenseFormat.  # noqa: E501
        :rtype: int
        """
        return self._min_resolution

    @min_resolution.setter
    def min_resolution(self, min_resolution):
        """Sets the min_resolution of this LicenseFormat.

        Width of the media, in pixels, allowed by this license  # noqa: E501

        :param min_resolution: The min_resolution of this LicenseFormat.  # noqa: E501
        :type: int
        """

        self._min_resolution = min_resolution

    @property
    def size(self):
        """Gets the size of this LicenseFormat.  # noqa: E501

        Keyword that details the size of the media, such as hd or sd for video, huge or vector for images  # noqa: E501

        :return: The size of this LicenseFormat.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LicenseFormat.

        Keyword that details the size of the media, such as hd or sd for video, huge or vector for images  # noqa: E501

        :param size: The size of this LicenseFormat.  # noqa: E501
        :type: str
        """

        self._size = size

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
        if issubclass(LicenseFormat, dict):
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
        if not isinstance(other, LicenseFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other