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

class LicenseEditorialContent(object):
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
        'editorial_id': 'str',
        'license': 'str',
        'metadata': 'LicenseRequestMetadata',
        'size': 'str'
    }

    attribute_map = {
        'editorial_id': 'editorial_id',
        'license': 'license',
        'metadata': 'metadata',
        'size': 'size'
    }

    def __init__(self, editorial_id=None, license=None, metadata=None, size='original'):  # noqa: E501
        """LicenseEditorialContent - a model defined in Swagger"""  # noqa: E501
        self._editorial_id = None
        self._license = None
        self._metadata = None
        self._size = None
        self.discriminator = None
        self.editorial_id = editorial_id
        self.license = license
        if metadata is not None:
            self.metadata = metadata
        if size is not None:
            self.size = size

    @property
    def editorial_id(self):
        """Gets the editorial_id of this LicenseEditorialContent.  # noqa: E501

        Editorial ID  # noqa: E501

        :return: The editorial_id of this LicenseEditorialContent.  # noqa: E501
        :rtype: str
        """
        return self._editorial_id

    @editorial_id.setter
    def editorial_id(self, editorial_id):
        """Sets the editorial_id of this LicenseEditorialContent.

        Editorial ID  # noqa: E501

        :param editorial_id: The editorial_id of this LicenseEditorialContent.  # noqa: E501
        :type: str
        """
        if editorial_id is None:
            raise ValueError("Invalid value for `editorial_id`, must not be `None`")  # noqa: E501

        self._editorial_id = editorial_id

    @property
    def license(self):
        """Gets the license of this LicenseEditorialContent.  # noqa: E501

        License agreement to use for licensing  # noqa: E501

        :return: The license of this LicenseEditorialContent.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this LicenseEditorialContent.

        License agreement to use for licensing  # noqa: E501

        :param license: The license of this LicenseEditorialContent.  # noqa: E501
        :type: str
        """
        if license is None:
            raise ValueError("Invalid value for `license`, must not be `None`")  # noqa: E501

        self._license = license

    @property
    def metadata(self):
        """Gets the metadata of this LicenseEditorialContent.  # noqa: E501


        :return: The metadata of this LicenseEditorialContent.  # noqa: E501
        :rtype: LicenseRequestMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this LicenseEditorialContent.


        :param metadata: The metadata of this LicenseEditorialContent.  # noqa: E501
        :type: LicenseRequestMetadata
        """

        self._metadata = metadata

    @property
    def size(self):
        """Gets the size of this LicenseEditorialContent.  # noqa: E501

        Asset size to download  # noqa: E501

        :return: The size of this LicenseEditorialContent.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LicenseEditorialContent.

        Asset size to download  # noqa: E501

        :param size: The size of this LicenseEditorialContent.  # noqa: E501
        :type: str
        """
        allowed_values = ["small", "medium", "original"]  # noqa: E501
        if size not in allowed_values:
            raise ValueError(
                "Invalid value for `size` ({0}), must be one of {1}"  # noqa: E501
                .format(size, allowed_values)
            )

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
        if issubclass(LicenseEditorialContent, dict):
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
        if not isinstance(other, LicenseEditorialContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
