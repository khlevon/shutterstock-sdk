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

class Subscription(object):
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
        'allotment': 'Allotment',
        'description': 'str',
        'expiration_time': 'datetime',
        'formats': 'list[LicenseFormat]',
        'id': 'str',
        'license': 'str',
        'asset_type': 'str',
        'metadata': 'SubscriptionMetadata',
        'price_per_download': 'Price'
    }

    attribute_map = {
        'allotment': 'allotment',
        'description': 'description',
        'expiration_time': 'expiration_time',
        'formats': 'formats',
        'id': 'id',
        'license': 'license',
        'asset_type': 'asset_type',
        'metadata': 'metadata',
        'price_per_download': 'price_per_download'
    }

    def __init__(self, allotment=None, description=None, expiration_time=None, formats=None, id=None, license=None, asset_type=None, metadata=None, price_per_download=None):  # noqa: E501
        """Subscription - a model defined in Swagger"""  # noqa: E501
        self._allotment = None
        self._description = None
        self._expiration_time = None
        self._formats = None
        self._id = None
        self._license = None
        self._asset_type = None
        self._metadata = None
        self._price_per_download = None
        self.discriminator = None
        if allotment is not None:
            self.allotment = allotment
        if description is not None:
            self.description = description
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if formats is not None:
            self.formats = formats
        self.id = id
        if license is not None:
            self.license = license
        if asset_type is not None:
            self.asset_type = asset_type
        if metadata is not None:
            self.metadata = metadata
        if price_per_download is not None:
            self.price_per_download = price_per_download

    @property
    def allotment(self):
        """Gets the allotment of this Subscription.  # noqa: E501


        :return: The allotment of this Subscription.  # noqa: E501
        :rtype: Allotment
        """
        return self._allotment

    @allotment.setter
    def allotment(self, allotment):
        """Sets the allotment of this Subscription.


        :param allotment: The allotment of this Subscription.  # noqa: E501
        :type: Allotment
        """

        self._allotment = allotment

    @property
    def description(self):
        """Gets the description of this Subscription.  # noqa: E501

        Description of the subscription  # noqa: E501

        :return: The description of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Subscription.

        Description of the subscription  # noqa: E501

        :param description: The description of this Subscription.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def expiration_time(self):
        """Gets the expiration_time of this Subscription.  # noqa: E501

        Date the subscription ends  # noqa: E501

        :return: The expiration_time of this Subscription.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this Subscription.

        Date the subscription ends  # noqa: E501

        :param expiration_time: The expiration_time of this Subscription.  # noqa: E501
        :type: datetime
        """

        self._expiration_time = expiration_time

    @property
    def formats(self):
        """Gets the formats of this Subscription.  # noqa: E501

        List of formats that are licensable for the subscription  # noqa: E501

        :return: The formats of this Subscription.  # noqa: E501
        :rtype: list[LicenseFormat]
        """
        return self._formats

    @formats.setter
    def formats(self, formats):
        """Sets the formats of this Subscription.

        List of formats that are licensable for the subscription  # noqa: E501

        :param formats: The formats of this Subscription.  # noqa: E501
        :type: list[LicenseFormat]
        """

        self._formats = formats

    @property
    def id(self):
        """Gets the id of this Subscription.  # noqa: E501

        Unique internal identifier for the subscription  # noqa: E501

        :return: The id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subscription.

        Unique internal identifier for the subscription  # noqa: E501

        :param id: The id of this Subscription.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def license(self):
        """Gets the license of this Subscription.  # noqa: E501

        Internal identifier for the type of subscription  # noqa: E501

        :return: The license of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this Subscription.

        Internal identifier for the type of subscription  # noqa: E501

        :param license: The license of this Subscription.  # noqa: E501
        :type: str
        """

        self._license = license

    @property
    def asset_type(self):
        """Gets the asset_type of this Subscription.  # noqa: E501

        Identifier for the type of assets associated with this subscription (images, videos, audio, editorial)  # noqa: E501

        :return: The asset_type of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this Subscription.

        Identifier for the type of assets associated with this subscription (images, videos, audio, editorial)  # noqa: E501

        :param asset_type: The asset_type of this Subscription.  # noqa: E501
        :type: str
        """

        self._asset_type = asset_type

    @property
    def metadata(self):
        """Gets the metadata of this Subscription.  # noqa: E501


        :return: The metadata of this Subscription.  # noqa: E501
        :rtype: SubscriptionMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Subscription.


        :param metadata: The metadata of this Subscription.  # noqa: E501
        :type: SubscriptionMetadata
        """

        self._metadata = metadata

    @property
    def price_per_download(self):
        """Gets the price_per_download of this Subscription.  # noqa: E501


        :return: The price_per_download of this Subscription.  # noqa: E501
        :rtype: Price
        """
        return self._price_per_download

    @price_per_download.setter
    def price_per_download(self, price_per_download):
        """Sets the price_per_download of this Subscription.


        :param price_per_download: The price_per_download of this Subscription.  # noqa: E501
        :type: Price
        """

        self._price_per_download = price_per_download

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
        if issubclass(Subscription, dict):
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
        if not isinstance(other, Subscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
