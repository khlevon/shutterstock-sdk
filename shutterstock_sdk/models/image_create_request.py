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

class ImageCreateRequest(object):
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
        'base64_image': 'str'
    }

    attribute_map = {
        'base64_image': 'base64_image'
    }

    def __init__(self, base64_image=None):  # noqa: E501
        """ImageCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._base64_image = None
        self.discriminator = None
        self.base64_image = base64_image

    @property
    def base64_image(self):
        """Gets the base64_image of this ImageCreateRequest.  # noqa: E501

        A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width or height  # noqa: E501

        :return: The base64_image of this ImageCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._base64_image

    @base64_image.setter
    def base64_image(self, base64_image):
        """Sets the base64_image of this ImageCreateRequest.

        A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width or height  # noqa: E501

        :param base64_image: The base64_image of this ImageCreateRequest.  # noqa: E501
        :type: str
        """
        if base64_image is None:
            raise ValueError("Invalid value for `base64_image`, must not be `None`")  # noqa: E501

        self._base64_image = base64_image

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
        if issubclass(ImageCreateRequest, dict):
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
        if not isinstance(other, ImageCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
