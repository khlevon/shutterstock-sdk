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

class AudioRendersFilesList(object):
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
        'filename': 'str',
        'bits_sample': 'float',
        'content_type': 'str',
        'download_url': 'str',
        'frequency_hz': 'float',
        'kbits_second': 'float',
        'size_bytes': 'float',
        'tracks': 'list[str]'
    }

    attribute_map = {
        'filename': 'filename',
        'bits_sample': 'bits_sample',
        'content_type': 'content_type',
        'download_url': 'download_url',
        'frequency_hz': 'frequency_hz',
        'kbits_second': 'kbits_second',
        'size_bytes': 'size_bytes',
        'tracks': 'tracks'
    }

    def __init__(self, filename=None, bits_sample=None, content_type=None, download_url=None, frequency_hz=None, kbits_second=None, size_bytes=None, tracks=None):  # noqa: E501
        """AudioRendersFilesList - a model defined in Swagger"""  # noqa: E501
        self._filename = None
        self._bits_sample = None
        self._content_type = None
        self._download_url = None
        self._frequency_hz = None
        self._kbits_second = None
        self._size_bytes = None
        self._tracks = None
        self.discriminator = None
        self.filename = filename
        self.bits_sample = bits_sample
        self.content_type = content_type
        self.download_url = download_url
        self.frequency_hz = frequency_hz
        self.kbits_second = kbits_second
        self.size_bytes = size_bytes
        self.tracks = tracks

    @property
    def filename(self):
        """Gets the filename of this AudioRendersFilesList.  # noqa: E501

        The user-specified file name suggestion from the render request; this file name becomes the filename property of the Content-Disposition header when the user downloads the rendered audio file  # noqa: E501

        :return: The filename of this AudioRendersFilesList.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this AudioRendersFilesList.

        The user-specified file name suggestion from the render request; this file name becomes the filename property of the Content-Disposition header when the user downloads the rendered audio file  # noqa: E501

        :param filename: The filename of this AudioRendersFilesList.  # noqa: E501
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    @property
    def bits_sample(self):
        """Gets the bits_sample of this AudioRendersFilesList.  # noqa: E501

        The bit depth of the audio files in bits/sample  # noqa: E501

        :return: The bits_sample of this AudioRendersFilesList.  # noqa: E501
        :rtype: float
        """
        return self._bits_sample

    @bits_sample.setter
    def bits_sample(self, bits_sample):
        """Sets the bits_sample of this AudioRendersFilesList.

        The bit depth of the audio files in bits/sample  # noqa: E501

        :param bits_sample: The bits_sample of this AudioRendersFilesList.  # noqa: E501
        :type: float
        """
        if bits_sample is None:
            raise ValueError("Invalid value for `bits_sample`, must not be `None`")  # noqa: E501

        self._bits_sample = bits_sample

    @property
    def content_type(self):
        """Gets the content_type of this AudioRendersFilesList.  # noqa: E501

        The content-type of the file  # noqa: E501

        :return: The content_type of this AudioRendersFilesList.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this AudioRendersFilesList.

        The content-type of the file  # noqa: E501

        :param content_type: The content_type of this AudioRendersFilesList.  # noqa: E501
        :type: str
        """
        if content_type is None:
            raise ValueError("Invalid value for `content_type`, must not be `None`")  # noqa: E501

        self._content_type = content_type

    @property
    def download_url(self):
        """Gets the download_url of this AudioRendersFilesList.  # noqa: E501

        The internet-accessible URL from which the file can be downloaded. Any redirects encountered when using this URL must be followed  # noqa: E501

        :return: The download_url of this AudioRendersFilesList.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this AudioRendersFilesList.

        The internet-accessible URL from which the file can be downloaded. Any redirects encountered when using this URL must be followed  # noqa: E501

        :param download_url: The download_url of this AudioRendersFilesList.  # noqa: E501
        :type: str
        """
        if download_url is None:
            raise ValueError("Invalid value for `download_url`, must not be `None`")  # noqa: E501

        self._download_url = download_url

    @property
    def frequency_hz(self):
        """Gets the frequency_hz of this AudioRendersFilesList.  # noqa: E501

        The Sample rate of the audio files in Hertz (Hz)  # noqa: E501

        :return: The frequency_hz of this AudioRendersFilesList.  # noqa: E501
        :rtype: float
        """
        return self._frequency_hz

    @frequency_hz.setter
    def frequency_hz(self, frequency_hz):
        """Sets the frequency_hz of this AudioRendersFilesList.

        The Sample rate of the audio files in Hertz (Hz)  # noqa: E501

        :param frequency_hz: The frequency_hz of this AudioRendersFilesList.  # noqa: E501
        :type: float
        """
        if frequency_hz is None:
            raise ValueError("Invalid value for `frequency_hz`, must not be `None`")  # noqa: E501

        self._frequency_hz = frequency_hz

    @property
    def kbits_second(self):
        """Gets the kbits_second of this AudioRendersFilesList.  # noqa: E501

        The data rate of the audio files in kilobits/second  # noqa: E501

        :return: The kbits_second of this AudioRendersFilesList.  # noqa: E501
        :rtype: float
        """
        return self._kbits_second

    @kbits_second.setter
    def kbits_second(self, kbits_second):
        """Sets the kbits_second of this AudioRendersFilesList.

        The data rate of the audio files in kilobits/second  # noqa: E501

        :param kbits_second: The kbits_second of this AudioRendersFilesList.  # noqa: E501
        :type: float
        """
        if kbits_second is None:
            raise ValueError("Invalid value for `kbits_second`, must not be `None`")  # noqa: E501

        self._kbits_second = kbits_second

    @property
    def size_bytes(self):
        """Gets the size_bytes of this AudioRendersFilesList.  # noqa: E501

        Size of the file in bytes  # noqa: E501

        :return: The size_bytes of this AudioRendersFilesList.  # noqa: E501
        :rtype: float
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this AudioRendersFilesList.

        Size of the file in bytes  # noqa: E501

        :param size_bytes: The size_bytes of this AudioRendersFilesList.  # noqa: E501
        :type: float
        """
        if size_bytes is None:
            raise ValueError("Invalid value for `size_bytes`, must not be `None`")  # noqa: E501

        self._size_bytes = size_bytes

    @property
    def tracks(self):
        """Gets the tracks of this AudioRendersFilesList.  # noqa: E501

        An array of track names included in the file  # noqa: E501

        :return: The tracks of this AudioRendersFilesList.  # noqa: E501
        :rtype: list[str]
        """
        return self._tracks

    @tracks.setter
    def tracks(self, tracks):
        """Sets the tracks of this AudioRendersFilesList.

        An array of track names included in the file  # noqa: E501

        :param tracks: The tracks of this AudioRendersFilesList.  # noqa: E501
        :type: list[str]
        """
        if tracks is None:
            raise ValueError("Invalid value for `tracks`, must not be `None`")  # noqa: E501

        self._tracks = tracks

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
        if issubclass(AudioRendersFilesList, dict):
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
        if not isinstance(other, AudioRendersFilesList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other