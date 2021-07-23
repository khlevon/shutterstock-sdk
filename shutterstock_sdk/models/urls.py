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

class Urls(object):
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
        'urls': 'list[str]'
    }

    attribute_map = {
        'urls': 'urls'
    }

    def __init__(self, urls=None):  # noqa: E501
        """Urls - a model defined in Swagger"""  # noqa: E501
        self._urls = None
        self.discriminator = None
        self.urls = urls

    @property
    def urls(self):
        """Gets the urls of this Urls.  # noqa: E501

        URLs  # noqa: E501

        :return: The urls of this Urls.  # noqa: E501
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this Urls.

        URLs  # noqa: E501

        :param urls: The urls of this Urls.  # noqa: E501
        :type: list[str]
        """
        if urls is None:
            raise ValueError("Invalid value for `urls`, must not be `None`")  # noqa: E501

        self._urls = urls

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
        if issubclass(Urls, dict):
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
        if not isinstance(other, Urls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other