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

class DownloadHistoryFormatDetails(object):
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
        'format': 'str',
        'size': 'str'
    }

    attribute_map = {
        'format': 'format',
        'size': 'size'
    }

    def __init__(self, format=None, size=None):  # noqa: E501
        """DownloadHistoryFormatDetails - a model defined in Swagger"""  # noqa: E501
        self._format = None
        self._size = None
        self.discriminator = None
        if format is not None:
            self.format = format
        if size is not None:
            self.size = size

    @property
    def format(self):
        """Gets the format of this DownloadHistoryFormatDetails.  # noqa: E501

        The format of the downloaded media  # noqa: E501

        :return: The format of this DownloadHistoryFormatDetails.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this DownloadHistoryFormatDetails.

        The format of the downloaded media  # noqa: E501

        :param format: The format of this DownloadHistoryFormatDetails.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def size(self):
        """Gets the size of this DownloadHistoryFormatDetails.  # noqa: E501

        The size of the downloaded media  # noqa: E501

        :return: The size of this DownloadHistoryFormatDetails.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DownloadHistoryFormatDetails.

        The size of the downloaded media  # noqa: E501

        :param size: The size of this DownloadHistoryFormatDetails.  # noqa: E501
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
        if issubclass(DownloadHistoryFormatDetails, dict):
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
        if not isinstance(other, DownloadHistoryFormatDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
