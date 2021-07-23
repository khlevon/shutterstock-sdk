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

class RedownloadVideo(object):
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
        'auth_cookie': 'Cookie',
        'show_modal': 'bool',
        'size': 'str',
        'verification_code': 'str'
    }

    attribute_map = {
        'auth_cookie': 'auth_cookie',
        'show_modal': 'show_modal',
        'size': 'size',
        'verification_code': 'verification_code'
    }

    def __init__(self, auth_cookie=None, show_modal=None, size=None, verification_code=None):  # noqa: E501
        """RedownloadVideo - a model defined in Swagger"""  # noqa: E501
        self._auth_cookie = None
        self._show_modal = None
        self._size = None
        self._verification_code = None
        self.discriminator = None
        if auth_cookie is not None:
            self.auth_cookie = auth_cookie
        if show_modal is not None:
            self.show_modal = show_modal
        if size is not None:
            self.size = size
        if verification_code is not None:
            self.verification_code = verification_code

    @property
    def auth_cookie(self):
        """Gets the auth_cookie of this RedownloadVideo.  # noqa: E501


        :return: The auth_cookie of this RedownloadVideo.  # noqa: E501
        :rtype: Cookie
        """
        return self._auth_cookie

    @auth_cookie.setter
    def auth_cookie(self, auth_cookie):
        """Sets the auth_cookie of this RedownloadVideo.


        :param auth_cookie: The auth_cookie of this RedownloadVideo.  # noqa: E501
        :type: Cookie
        """

        self._auth_cookie = auth_cookie

    @property
    def show_modal(self):
        """Gets the show_modal of this RedownloadVideo.  # noqa: E501

        (Deprecated)  # noqa: E501

        :return: The show_modal of this RedownloadVideo.  # noqa: E501
        :rtype: bool
        """
        return self._show_modal

    @show_modal.setter
    def show_modal(self, show_modal):
        """Sets the show_modal of this RedownloadVideo.

        (Deprecated)  # noqa: E501

        :param show_modal: The show_modal of this RedownloadVideo.  # noqa: E501
        :type: bool
        """

        self._show_modal = show_modal

    @property
    def size(self):
        """Gets the size of this RedownloadVideo.  # noqa: E501

        Size of the video  # noqa: E501

        :return: The size of this RedownloadVideo.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this RedownloadVideo.

        Size of the video  # noqa: E501

        :param size: The size of this RedownloadVideo.  # noqa: E501
        :type: str
        """
        allowed_values = ["web", "sd", "hd", "4k"]  # noqa: E501
        if size not in allowed_values:
            raise ValueError(
                "Invalid value for `size` ({0}), must be one of {1}"  # noqa: E501
                .format(size, allowed_values)
            )

        self._size = size

    @property
    def verification_code(self):
        """Gets the verification_code of this RedownloadVideo.  # noqa: E501

        (Deprecated)  # noqa: E501

        :return: The verification_code of this RedownloadVideo.  # noqa: E501
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        """Sets the verification_code of this RedownloadVideo.

        (Deprecated)  # noqa: E501

        :param verification_code: The verification_code of this RedownloadVideo.  # noqa: E501
        :type: str
        """

        self._verification_code = verification_code

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
        if issubclass(RedownloadVideo, dict):
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
        if not isinstance(other, RedownloadVideo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
