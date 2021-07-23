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

class VideoSizeDetails(object):
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
        'display_name': 'str',
        'file_size': 'int',
        'format': 'str',
        'fps': 'float',
        'height': 'int',
        'is_licensable': 'bool',
        'width': 'int'
    }

    attribute_map = {
        'display_name': 'display_name',
        'file_size': 'file_size',
        'format': 'format',
        'fps': 'fps',
        'height': 'height',
        'is_licensable': 'is_licensable',
        'width': 'width'
    }

    def __init__(self, display_name=None, file_size=None, format=None, fps=None, height=None, is_licensable=None, width=None):  # noqa: E501
        """VideoSizeDetails - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._file_size = None
        self._format = None
        self._fps = None
        self._height = None
        self._is_licensable = None
        self._width = None
        self.discriminator = None
        if display_name is not None:
            self.display_name = display_name
        if file_size is not None:
            self.file_size = file_size
        if format is not None:
            self.format = format
        if fps is not None:
            self.fps = fps
        if height is not None:
            self.height = height
        if is_licensable is not None:
            self.is_licensable = is_licensable
        if width is not None:
            self.width = width

    @property
    def display_name(self):
        """Gets the display_name of this VideoSizeDetails.  # noqa: E501

        Display name of this video size  # noqa: E501

        :return: The display_name of this VideoSizeDetails.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this VideoSizeDetails.

        Display name of this video size  # noqa: E501

        :param display_name: The display_name of this VideoSizeDetails.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def file_size(self):
        """Gets the file_size of this VideoSizeDetails.  # noqa: E501

        File size (in bytes) of this video size  # noqa: E501

        :return: The file_size of this VideoSizeDetails.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this VideoSizeDetails.

        File size (in bytes) of this video size  # noqa: E501

        :param file_size: The file_size of this VideoSizeDetails.  # noqa: E501
        :type: int
        """

        self._file_size = file_size

    @property
    def format(self):
        """Gets the format of this VideoSizeDetails.  # noqa: E501

        Format of this video size  # noqa: E501

        :return: The format of this VideoSizeDetails.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this VideoSizeDetails.

        Format of this video size  # noqa: E501

        :param format: The format of this VideoSizeDetails.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def fps(self):
        """Gets the fps of this VideoSizeDetails.  # noqa: E501

        Frames per second of this video size  # noqa: E501

        :return: The fps of this VideoSizeDetails.  # noqa: E501
        :rtype: float
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        """Sets the fps of this VideoSizeDetails.

        Frames per second of this video size  # noqa: E501

        :param fps: The fps of this VideoSizeDetails.  # noqa: E501
        :type: float
        """

        self._fps = fps

    @property
    def height(self):
        """Gets the height of this VideoSizeDetails.  # noqa: E501

        Height of this video size  # noqa: E501

        :return: The height of this VideoSizeDetails.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this VideoSizeDetails.

        Height of this video size  # noqa: E501

        :param height: The height of this VideoSizeDetails.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def is_licensable(self):
        """Gets the is_licensable of this VideoSizeDetails.  # noqa: E501

        Whether or not videos can be licensed in this video size  # noqa: E501

        :return: The is_licensable of this VideoSizeDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_licensable

    @is_licensable.setter
    def is_licensable(self, is_licensable):
        """Sets the is_licensable of this VideoSizeDetails.

        Whether or not videos can be licensed in this video size  # noqa: E501

        :param is_licensable: The is_licensable of this VideoSizeDetails.  # noqa: E501
        :type: bool
        """

        self._is_licensable = is_licensable

    @property
    def width(self):
        """Gets the width of this VideoSizeDetails.  # noqa: E501

        Width of this video size  # noqa: E501

        :return: The width of this VideoSizeDetails.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this VideoSizeDetails.

        Width of this video size  # noqa: E501

        :param width: The width of this VideoSizeDetails.  # noqa: E501
        :type: int
        """

        self._width = width

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
        if issubclass(VideoSizeDetails, dict):
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
        if not isinstance(other, VideoSizeDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
