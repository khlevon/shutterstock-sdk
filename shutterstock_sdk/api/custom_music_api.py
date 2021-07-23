# coding: utf-8

"""
    Shutterstock API Explorer

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.  # noqa: E501

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from shutterstock_sdk.api_client import ApiClient


class CustomMusicApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_audio_renders(self, body, **kwargs):  # noqa: E501
        """Create rendered audio  # noqa: E501

        This endpoint creates rendered audio from timeline data. It returns a render ID that you can use to download the finished audio when it is ready. The render ID is valid for up to 48 hours.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_audio_renders(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateAudioRendersRequest body: Parameters for the audio, including the timeline and information about the output file (required)
        :return: AudioRendersListResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_audio_renders_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_audio_renders_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_audio_renders_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create rendered audio  # noqa: E501

        This endpoint creates rendered audio from timeline data. It returns a render ID that you can use to download the finished audio when it is ready. The render ID is valid for up to 48 hours.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_audio_renders_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateAudioRendersRequest body: Parameters for the audio, including the timeline and information about the output file (required)
        :return: AudioRendersListResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_audio_renders" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_audio_renders`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic', 'customer_accessCode']  # noqa: E501

        return self.api_client.call_api(
            '/v2/ai/audio/renders', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AudioRendersListResults',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_renders(self, id, **kwargs):  # noqa: E501
        """Get details about audio renders  # noqa: E501

        This endpoint shows the status of one or more audio renders, including download links for completed audio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_renders(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] id: One or more render IDs (required)
        :return: AudioRendersListResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_renders_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_renders_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def fetch_renders_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get details about audio renders  # noqa: E501

        This endpoint shows the status of one or more audio renders, including download links for completed audio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_renders_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] id: One or more render IDs (required)
        :return: AudioRendersListResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_renders" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `fetch_renders`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
            collection_formats['id'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic', 'customer_accessCode']  # noqa: E501

        return self.api_client.call_api(
            '/v2/ai/audio/renders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AudioRendersListResults',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_custom_descriptors(self, **kwargs):  # noqa: E501
        """List computer audio descriptors  # noqa: E501

        This endpoint lists the descriptors that you can use in the audio regions in an audio render.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_custom_descriptors(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float render_speed_over: Show descriptors with an average render speed that is greater than or equal to the specified value
        :param str band_id: Show descriptors that contain the specified band (case-sentsitive)
        :param str band_name: Show descriptors with the specified band name (case-sensitive)
        :param int page: Page number
        :param int per_page: Number of results per page
        :param list[str] id: Show descriptors with the specified IDs (case-sensitive)
        :param str instrument_name: Show descriptors with the specified instrument name (case-sensitive)
        :param str instrument_id: Show descriptors with the specified instrument ID (case-sensitive)
        :param float tempo: Show descriptors whose tempo range includes the specified tempo in beats per minute
        :param float tempo_to: Show descriptors with a tempo that is less than or equal to the specified number
        :param float tempo_from: Show descriptors that have a tempo range that includes the specified tempo in beats per minute
        :param str name: Show descriptors with the specified name (case-sensitive)
        :param str tag: Show descriptors with the specified tag, such as Cinematic or Roomy (case-sensitive)
        :return: DescriptorsListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_custom_descriptors_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_custom_descriptors_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_custom_descriptors_with_http_info(self, **kwargs):  # noqa: E501
        """List computer audio descriptors  # noqa: E501

        This endpoint lists the descriptors that you can use in the audio regions in an audio render.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_custom_descriptors_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float render_speed_over: Show descriptors with an average render speed that is greater than or equal to the specified value
        :param str band_id: Show descriptors that contain the specified band (case-sentsitive)
        :param str band_name: Show descriptors with the specified band name (case-sensitive)
        :param int page: Page number
        :param int per_page: Number of results per page
        :param list[str] id: Show descriptors with the specified IDs (case-sensitive)
        :param str instrument_name: Show descriptors with the specified instrument name (case-sensitive)
        :param str instrument_id: Show descriptors with the specified instrument ID (case-sensitive)
        :param float tempo: Show descriptors whose tempo range includes the specified tempo in beats per minute
        :param float tempo_to: Show descriptors with a tempo that is less than or equal to the specified number
        :param float tempo_from: Show descriptors that have a tempo range that includes the specified tempo in beats per minute
        :param str name: Show descriptors with the specified name (case-sensitive)
        :param str tag: Show descriptors with the specified tag, such as Cinematic or Roomy (case-sensitive)
        :return: DescriptorsListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['render_speed_over', 'band_id', 'band_name', 'page', 'per_page', 'id', 'instrument_name', 'instrument_id', 'tempo', 'tempo_to', 'tempo_from', 'name', 'tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_custom_descriptors" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'render_speed_over' in params:
            query_params.append(('render_speed_over', params['render_speed_over']))  # noqa: E501
        if 'band_id' in params:
            query_params.append(('band_id', params['band_id']))  # noqa: E501
        if 'band_name' in params:
            query_params.append(('band_name', params['band_name']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
            collection_formats['id'] = 'multi'  # noqa: E501
        if 'instrument_name' in params:
            query_params.append(('instrument_name', params['instrument_name']))  # noqa: E501
        if 'instrument_id' in params:
            query_params.append(('instrument_id', params['instrument_id']))  # noqa: E501
        if 'tempo' in params:
            query_params.append(('tempo', params['tempo']))  # noqa: E501
        if 'tempo_to' in params:
            query_params.append(('tempo_to', params['tempo_to']))  # noqa: E501
        if 'tempo_from' in params:
            query_params.append(('tempo_from', params['tempo_from']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic', 'customer_accessCode']  # noqa: E501

        return self.api_client.call_api(
            '/v2/ai/audio/descriptors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DescriptorsListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_custom_instruments(self, **kwargs):  # noqa: E501
        """List computer audio instruments  # noqa: E501

        This endpoint lists the instruments that you can include in computer audio. If you specify more than one search parameter, the API uses an AND condition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_custom_instruments(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] id: Show instruments with the specified ID
        :param int per_page: Number of results per page
        :param int page: Page number
        :param str name: Show instruments with the specified name (case-sensitive)
        :param str tag: Show instruments with the specified tag, such as Percussion or Strings (case-sensitive)
        :return: InstrumentsListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_custom_instruments_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_custom_instruments_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_custom_instruments_with_http_info(self, **kwargs):  # noqa: E501
        """List computer audio instruments  # noqa: E501

        This endpoint lists the instruments that you can include in computer audio. If you specify more than one search parameter, the API uses an AND condition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_custom_instruments_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] id: Show instruments with the specified ID
        :param int per_page: Number of results per page
        :param int page: Page number
        :param str name: Show instruments with the specified name (case-sensitive)
        :param str tag: Show instruments with the specified tag, such as Percussion or Strings (case-sensitive)
        :return: InstrumentsListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'per_page', 'page', 'name', 'tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_custom_instruments" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
            collection_formats['id'] = 'multi'  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic', 'customer_accessCode']  # noqa: E501

        return self.api_client.call_api(
            '/v2/ai/audio/instruments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InstrumentsListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
