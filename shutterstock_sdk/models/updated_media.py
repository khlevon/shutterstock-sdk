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

class UpdatedMedia(object):
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
        'id': 'str',
        'updated_time': 'datetime',
        'updates': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'updated_time': 'updated_time',
        'updates': 'updates'
    }

    def __init__(self, id=None, updated_time=None, updates=None):  # noqa: E501
        """UpdatedMedia - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._updated_time = None
        self._updates = None
        self.discriminator = None
        self.id = id
        self.updated_time = updated_time
        self.updates = updates

    @property
    def id(self):
        """Gets the id of this UpdatedMedia.  # noqa: E501

        ID of the media  # noqa: E501

        :return: The id of this UpdatedMedia.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdatedMedia.

        ID of the media  # noqa: E501

        :param id: The id of this UpdatedMedia.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def updated_time(self):
        """Gets the updated_time of this UpdatedMedia.  # noqa: E501

        Date that the media was updated  # noqa: E501

        :return: The updated_time of this UpdatedMedia.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this UpdatedMedia.

        Date that the media was updated  # noqa: E501

        :param updated_time: The updated_time of this UpdatedMedia.  # noqa: E501
        :type: datetime
        """
        if updated_time is None:
            raise ValueError("Invalid value for `updated_time`, must not be `None`")  # noqa: E501

        self._updated_time = updated_time

    @property
    def updates(self):
        """Gets the updates of this UpdatedMedia.  # noqa: E501

        Types of updates that were made to the piece of media  # noqa: E501

        :return: The updates of this UpdatedMedia.  # noqa: E501
        :rtype: list[str]
        """
        return self._updates

    @updates.setter
    def updates(self, updates):
        """Sets the updates of this UpdatedMedia.

        Types of updates that were made to the piece of media  # noqa: E501

        :param updates: The updates of this UpdatedMedia.  # noqa: E501
        :type: list[str]
        """
        if updates is None:
            raise ValueError("Invalid value for `updates`, must not be `None`")  # noqa: E501

        self._updates = updates

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
        if issubclass(UpdatedMedia, dict):
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
        if not isinstance(other, UpdatedMedia):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
