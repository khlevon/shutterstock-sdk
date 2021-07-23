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

class ContributorProfile(object):
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
        'about': 'str',
        'contributor_type': 'list[str]',
        'display_name': 'str',
        'equipment': 'list[str]',
        'id': 'str',
        'location': 'str',
        'portfolio_url': 'str',
        'social_media': 'ContributorProfileSocialMedia',
        'styles': 'list[str]',
        'subjects': 'list[str]',
        'website': 'str'
    }

    attribute_map = {
        'about': 'about',
        'contributor_type': 'contributor_type',
        'display_name': 'display_name',
        'equipment': 'equipment',
        'id': 'id',
        'location': 'location',
        'portfolio_url': 'portfolio_url',
        'social_media': 'social_media',
        'styles': 'styles',
        'subjects': 'subjects',
        'website': 'website'
    }

    def __init__(self, about=None, contributor_type=None, display_name=None, equipment=None, id=None, location=None, portfolio_url=None, social_media=None, styles=None, subjects=None, website=None):  # noqa: E501
        """ContributorProfile - a model defined in Swagger"""  # noqa: E501
        self._about = None
        self._contributor_type = None
        self._display_name = None
        self._equipment = None
        self._id = None
        self._location = None
        self._portfolio_url = None
        self._social_media = None
        self._styles = None
        self._subjects = None
        self._website = None
        self.discriminator = None
        if about is not None:
            self.about = about
        if contributor_type is not None:
            self.contributor_type = contributor_type
        if display_name is not None:
            self.display_name = display_name
        if equipment is not None:
            self.equipment = equipment
        self.id = id
        if location is not None:
            self.location = location
        if portfolio_url is not None:
            self.portfolio_url = portfolio_url
        if social_media is not None:
            self.social_media = social_media
        if styles is not None:
            self.styles = styles
        if subjects is not None:
            self.subjects = subjects
        if website is not None:
            self.website = website

    @property
    def about(self):
        """Gets the about of this ContributorProfile.  # noqa: E501

        Short description of the contributors' library  # noqa: E501

        :return: The about of this ContributorProfile.  # noqa: E501
        :rtype: str
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this ContributorProfile.

        Short description of the contributors' library  # noqa: E501

        :param about: The about of this ContributorProfile.  # noqa: E501
        :type: str
        """

        self._about = about

    @property
    def contributor_type(self):
        """Gets the contributor_type of this ContributorProfile.  # noqa: E501

        Type of content that the contributor specializes in (photographer, illustrator, etc)  # noqa: E501

        :return: The contributor_type of this ContributorProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._contributor_type

    @contributor_type.setter
    def contributor_type(self, contributor_type):
        """Sets the contributor_type of this ContributorProfile.

        Type of content that the contributor specializes in (photographer, illustrator, etc)  # noqa: E501

        :param contributor_type: The contributor_type of this ContributorProfile.  # noqa: E501
        :type: list[str]
        """

        self._contributor_type = contributor_type

    @property
    def display_name(self):
        """Gets the display_name of this ContributorProfile.  # noqa: E501

        Preferred name to be displayed for the contributor  # noqa: E501

        :return: The display_name of this ContributorProfile.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ContributorProfile.

        Preferred name to be displayed for the contributor  # noqa: E501

        :param display_name: The display_name of this ContributorProfile.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def equipment(self):
        """Gets the equipment of this ContributorProfile.  # noqa: E501

        List of equipment used by the contributor (Canon EOS 5D Mark II, etc)  # noqa: E501

        :return: The equipment of this ContributorProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this ContributorProfile.

        List of equipment used by the contributor (Canon EOS 5D Mark II, etc)  # noqa: E501

        :param equipment: The equipment of this ContributorProfile.  # noqa: E501
        :type: list[str]
        """

        self._equipment = equipment

    @property
    def id(self):
        """Gets the id of this ContributorProfile.  # noqa: E501

        Contributor ID  # noqa: E501

        :return: The id of this ContributorProfile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContributorProfile.

        Contributor ID  # noqa: E501

        :param id: The id of this ContributorProfile.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def location(self):
        """Gets the location of this ContributorProfile.  # noqa: E501

        Country code representing the contributor's locale  # noqa: E501

        :return: The location of this ContributorProfile.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ContributorProfile.

        Country code representing the contributor's locale  # noqa: E501

        :param location: The location of this ContributorProfile.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def portfolio_url(self):
        """Gets the portfolio_url of this ContributorProfile.  # noqa: E501

        Web URL for the contributors' profile  # noqa: E501

        :return: The portfolio_url of this ContributorProfile.  # noqa: E501
        :rtype: str
        """
        return self._portfolio_url

    @portfolio_url.setter
    def portfolio_url(self, portfolio_url):
        """Sets the portfolio_url of this ContributorProfile.

        Web URL for the contributors' profile  # noqa: E501

        :param portfolio_url: The portfolio_url of this ContributorProfile.  # noqa: E501
        :type: str
        """

        self._portfolio_url = portfolio_url

    @property
    def social_media(self):
        """Gets the social_media of this ContributorProfile.  # noqa: E501


        :return: The social_media of this ContributorProfile.  # noqa: E501
        :rtype: ContributorProfileSocialMedia
        """
        return self._social_media

    @social_media.setter
    def social_media(self, social_media):
        """Sets the social_media of this ContributorProfile.


        :param social_media: The social_media of this ContributorProfile.  # noqa: E501
        :type: ContributorProfileSocialMedia
        """

        self._social_media = social_media

    @property
    def styles(self):
        """Gets the styles of this ContributorProfile.  # noqa: E501

        List of styles that the contributor specializes in (lifestyle, mixed media, etc)  # noqa: E501

        :return: The styles of this ContributorProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._styles

    @styles.setter
    def styles(self, styles):
        """Sets the styles of this ContributorProfile.

        List of styles that the contributor specializes in (lifestyle, mixed media, etc)  # noqa: E501

        :param styles: The styles of this ContributorProfile.  # noqa: E501
        :type: list[str]
        """

        self._styles = styles

    @property
    def subjects(self):
        """Gets the subjects of this ContributorProfile.  # noqa: E501

        Generic list of subjects for contributors' work (food_and_drink, holiday, people, etc)  # noqa: E501

        :return: The subjects of this ContributorProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._subjects

    @subjects.setter
    def subjects(self, subjects):
        """Sets the subjects of this ContributorProfile.

        Generic list of subjects for contributors' work (food_and_drink, holiday, people, etc)  # noqa: E501

        :param subjects: The subjects of this ContributorProfile.  # noqa: E501
        :type: list[str]
        """

        self._subjects = subjects

    @property
    def website(self):
        """Gets the website of this ContributorProfile.  # noqa: E501

        Personal website for the contributor  # noqa: E501

        :return: The website of this ContributorProfile.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this ContributorProfile.

        Personal website for the contributor  # noqa: E501

        :param website: The website of this ContributorProfile.  # noqa: E501
        :type: str
        """

        self._website = website

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
        if issubclass(ContributorProfile, dict):
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
        if not isinstance(other, ContributorProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other