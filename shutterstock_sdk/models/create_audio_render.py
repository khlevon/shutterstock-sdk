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

class CreateAudioRender(object):
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
        'preset': 'str',
        'filename': 'str',
        'timeline': 'AudioRenderTimeline'
    }

    attribute_map = {
        'preset': 'preset',
        'filename': 'filename',
        'timeline': 'timeline'
    }

    def __init__(self, preset=None, filename=None, timeline=None):  # noqa: E501
        """CreateAudioRender - a model defined in Swagger"""  # noqa: E501
        self._preset = None
        self._filename = None
        self._timeline = None
        self.discriminator = None
        self.preset = preset
        self.filename = filename
        self.timeline = timeline

    @property
    def preset(self):
        """Gets the preset of this CreateAudioRender.  # noqa: E501

        File format, such as MP3 file, combined WAV file, or individual track WAV files  # noqa: E501

        :return: The preset of this CreateAudioRender.  # noqa: E501
        :rtype: str
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        """Sets the preset of this CreateAudioRender.

        File format, such as MP3 file, combined WAV file, or individual track WAV files  # noqa: E501

        :param preset: The preset of this CreateAudioRender.  # noqa: E501
        :type: str
        """
        if preset is None:
            raise ValueError("Invalid value for `preset`, must not be `None`")  # noqa: E501
        allowed_values = ["MASTER_MP3", "MASTER_WAV", "STEMS_WAV"]  # noqa: E501
        if preset not in allowed_values:
            raise ValueError(
                "Invalid value for `preset` ({0}), must be one of {1}"  # noqa: E501
                .format(preset, allowed_values)
            )

        self._preset = preset

    @property
    def filename(self):
        """Gets the filename of this CreateAudioRender.  # noqa: E501

        A user-specified file name suggestion; this file name becomes the filename property of the Content-Disposition header when the user downloads the rendered audio file  # noqa: E501

        :return: The filename of this CreateAudioRender.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this CreateAudioRender.

        A user-specified file name suggestion; this file name becomes the filename property of the Content-Disposition header when the user downloads the rendered audio file  # noqa: E501

        :param filename: The filename of this CreateAudioRender.  # noqa: E501
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    @property
    def timeline(self):
        """Gets the timeline of this CreateAudioRender.  # noqa: E501


        :return: The timeline of this CreateAudioRender.  # noqa: E501
        :rtype: AudioRenderTimeline
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        """Sets the timeline of this CreateAudioRender.


        :param timeline: The timeline of this CreateAudioRender.  # noqa: E501
        :type: AudioRenderTimeline
        """
        if timeline is None:
            raise ValueError("Invalid value for `timeline`, must not be `None`")  # noqa: E501

        self._timeline = timeline

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
        if issubclass(CreateAudioRender, dict):
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
        if not isinstance(other, CreateAudioRender):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
