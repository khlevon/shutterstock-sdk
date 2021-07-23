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

class Error(object):
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
        'code': 'str',
        'data': 'str',
        'items': 'list[object]',
        'message': 'str',
        'path': 'str'
    }

    attribute_map = {
        'code': 'code',
        'data': 'data',
        'items': 'items',
        'message': 'message',
        'path': 'path'
    }

    def __init__(self, code=None, data=None, items=None, message=None, path=None):  # noqa: E501
        """Error - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._data = None
        self._items = None
        self._message = None
        self._path = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if data is not None:
            self.data = data
        if items is not None:
            self.items = items
        self.message = message
        if path is not None:
            self.path = path

    @property
    def code(self):
        """Gets the code of this Error.  # noqa: E501

        The error code of this error  # noqa: E501

        :return: The code of this Error.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Error.

        The error code of this error  # noqa: E501

        :param code: The code of this Error.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def data(self):
        """Gets the data of this Error.  # noqa: E501

        Debugging information about the error  # noqa: E501

        :return: The data of this Error.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Error.

        Debugging information about the error  # noqa: E501

        :param data: The data of this Error.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def items(self):
        """Gets the items of this Error.  # noqa: E501

        A list of items that produced the error  # noqa: E501

        :return: The items of this Error.  # noqa: E501
        :rtype: list[object]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Error.

        A list of items that produced the error  # noqa: E501

        :param items: The items of this Error.  # noqa: E501
        :type: list[object]
        """

        self._items = items

    @property
    def message(self):
        """Gets the message of this Error.  # noqa: E501

        Specific details about this error  # noqa: E501

        :return: The message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Error.

        Specific details about this error  # noqa: E501

        :param message: The message of this Error.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def path(self):
        """Gets the path of this Error.  # noqa: E501

        Internal code reference to the source of the error  # noqa: E501

        :return: The path of this Error.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Error.

        Internal code reference to the source of the error  # noqa: E501

        :param path: The path of this Error.  # noqa: E501
        :type: str
        """

        self._path = path

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
        if issubclass(Error, dict):
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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other