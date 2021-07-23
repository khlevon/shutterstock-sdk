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

class LicenseImageResult(object):
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
        'allotment_charge': 'int',
        'download': 'Url',
        'error': 'str',
        'image_id': 'str',
        'price': 'Price'
    }

    attribute_map = {
        'allotment_charge': 'allotment_charge',
        'download': 'download',
        'error': 'error',
        'image_id': 'image_id',
        'price': 'price'
    }

    def __init__(self, allotment_charge=None, download=None, error=None, image_id=None, price=None):  # noqa: E501
        """LicenseImageResult - a model defined in Swagger"""  # noqa: E501
        self._allotment_charge = None
        self._download = None
        self._error = None
        self._image_id = None
        self._price = None
        self.discriminator = None
        if allotment_charge is not None:
            self.allotment_charge = allotment_charge
        if download is not None:
            self.download = download
        if error is not None:
            self.error = error
        self.image_id = image_id
        if price is not None:
            self.price = price

    @property
    def allotment_charge(self):
        """Gets the allotment_charge of this LicenseImageResult.  # noqa: E501

        Number of credits that this licensing event used  # noqa: E501

        :return: The allotment_charge of this LicenseImageResult.  # noqa: E501
        :rtype: int
        """
        return self._allotment_charge

    @allotment_charge.setter
    def allotment_charge(self, allotment_charge):
        """Sets the allotment_charge of this LicenseImageResult.

        Number of credits that this licensing event used  # noqa: E501

        :param allotment_charge: The allotment_charge of this LicenseImageResult.  # noqa: E501
        :type: int
        """

        self._allotment_charge = allotment_charge

    @property
    def download(self):
        """Gets the download of this LicenseImageResult.  # noqa: E501


        :return: The download of this LicenseImageResult.  # noqa: E501
        :rtype: Url
        """
        return self._download

    @download.setter
    def download(self, download):
        """Sets the download of this LicenseImageResult.


        :param download: The download of this LicenseImageResult.  # noqa: E501
        :type: Url
        """

        self._download = download

    @property
    def error(self):
        """Gets the error of this LicenseImageResult.  # noqa: E501

        Error message, appears only if there was an error  # noqa: E501

        :return: The error of this LicenseImageResult.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this LicenseImageResult.

        Error message, appears only if there was an error  # noqa: E501

        :param error: The error of this LicenseImageResult.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def image_id(self):
        """Gets the image_id of this LicenseImageResult.  # noqa: E501

        Image ID that was licensed  # noqa: E501

        :return: The image_id of this LicenseImageResult.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this LicenseImageResult.

        Image ID that was licensed  # noqa: E501

        :param image_id: The image_id of this LicenseImageResult.  # noqa: E501
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def price(self):
        """Gets the price of this LicenseImageResult.  # noqa: E501


        :return: The price of this LicenseImageResult.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this LicenseImageResult.


        :param price: The price of this LicenseImageResult.  # noqa: E501
        :type: Price
        """

        self._price = price

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
        if issubclass(LicenseImageResult, dict):
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
        if not isinstance(other, LicenseImageResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
