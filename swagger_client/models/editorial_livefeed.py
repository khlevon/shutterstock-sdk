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

class EditorialLivefeed(object):
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
        'cover_item': 'EditorialCoverItem',
        'created_time': 'datetime',
        'id': 'str',
        'name': 'str',
        'total_item_count': 'int'
    }

    attribute_map = {
        'cover_item': 'cover_item',
        'created_time': 'created_time',
        'id': 'id',
        'name': 'name',
        'total_item_count': 'total_item_count'
    }

    def __init__(self, cover_item=None, created_time=None, id=None, name=None, total_item_count=None):  # noqa: E501
        """EditorialLivefeed - a model defined in Swagger"""  # noqa: E501
        self._cover_item = None
        self._created_time = None
        self._id = None
        self._name = None
        self._total_item_count = None
        self.discriminator = None
        if cover_item is not None:
            self.cover_item = cover_item
        if created_time is not None:
            self.created_time = created_time
        self.id = id
        self.name = name
        self.total_item_count = total_item_count

    @property
    def cover_item(self):
        """Gets the cover_item of this EditorialLivefeed.  # noqa: E501


        :return: The cover_item of this EditorialLivefeed.  # noqa: E501
        :rtype: EditorialCoverItem
        """
        return self._cover_item

    @cover_item.setter
    def cover_item(self, cover_item):
        """Sets the cover_item of this EditorialLivefeed.


        :param cover_item: The cover_item of this EditorialLivefeed.  # noqa: E501
        :type: EditorialCoverItem
        """

        self._cover_item = cover_item

    @property
    def created_time(self):
        """Gets the created_time of this EditorialLivefeed.  # noqa: E501

        When the livefeed was initially created  # noqa: E501

        :return: The created_time of this EditorialLivefeed.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EditorialLivefeed.

        When the livefeed was initially created  # noqa: E501

        :param created_time: The created_time of this EditorialLivefeed.  # noqa: E501
        :type: datetime
        """

        self._created_time = created_time

    @property
    def id(self):
        """Gets the id of this EditorialLivefeed.  # noqa: E501

        Livefeed ID  # noqa: E501

        :return: The id of this EditorialLivefeed.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EditorialLivefeed.

        Livefeed ID  # noqa: E501

        :param id: The id of this EditorialLivefeed.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this EditorialLivefeed.  # noqa: E501

        Name of the livefeed  # noqa: E501

        :return: The name of this EditorialLivefeed.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EditorialLivefeed.

        Name of the livefeed  # noqa: E501

        :param name: The name of this EditorialLivefeed.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def total_item_count(self):
        """Gets the total_item_count of this EditorialLivefeed.  # noqa: E501

        Total count of items in the livefeed  # noqa: E501

        :return: The total_item_count of this EditorialLivefeed.  # noqa: E501
        :rtype: int
        """
        return self._total_item_count

    @total_item_count.setter
    def total_item_count(self, total_item_count):
        """Sets the total_item_count of this EditorialLivefeed.

        Total count of items in the livefeed  # noqa: E501

        :param total_item_count: The total_item_count of this EditorialLivefeed.  # noqa: E501
        :type: int
        """
        if total_item_count is None:
            raise ValueError("Invalid value for `total_item_count`, must not be `None`")  # noqa: E501

        self._total_item_count = total_item_count

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
        if issubclass(EditorialLivefeed, dict):
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
        if not isinstance(other, EditorialLivefeed):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
