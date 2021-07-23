# swagger_client.CustomMusicApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audio_renders**](CustomMusicApi.md#create_audio_renders) | **POST** /v2/ai/audio/renders | Create rendered audio
[**fetch_renders**](CustomMusicApi.md#fetch_renders) | **GET** /v2/ai/audio/renders | Get details about audio renders
[**list_custom_descriptors**](CustomMusicApi.md#list_custom_descriptors) | **GET** /v2/ai/audio/descriptors | List computer audio descriptors
[**list_custom_instruments**](CustomMusicApi.md#list_custom_instruments) | **GET** /v2/ai/audio/instruments | List computer audio instruments

# **create_audio_renders**
> AudioRendersListResults create_audio_renders(body)

Create rendered audio

This endpoint creates rendered audio from timeline data. It returns a render ID that you can use to download the finished audio when it is ready. The render ID is valid for up to 48 hours.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: customer_accessCode
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CustomMusicApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateAudioRendersRequest() # CreateAudioRendersRequest | Parameters for the audio, including the timeline and information about the output file

try:
    # Create rendered audio
    api_response = api_instance.create_audio_renders(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomMusicApi->create_audio_renders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAudioRendersRequest**](CreateAudioRendersRequest.md)| Parameters for the audio, including the timeline and information about the output file | 

### Return type

[**AudioRendersListResults**](AudioRendersListResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_renders**
> AudioRendersListResults fetch_renders(id)

Get details about audio renders

This endpoint shows the status of one or more audio renders, including download links for completed audio.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: customer_accessCode
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CustomMusicApi(swagger_client.ApiClient(configuration))
id = ['id_example'] # list[str] | One or more render IDs

try:
    # Get details about audio renders
    api_response = api_instance.fetch_renders(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomMusicApi->fetch_renders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| One or more render IDs | 

### Return type

[**AudioRendersListResults**](AudioRendersListResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_descriptors**
> DescriptorsListResult list_custom_descriptors(render_speed_over=render_speed_over, band_id=band_id, band_name=band_name, page=page, per_page=per_page, id=id, instrument_name=instrument_name, instrument_id=instrument_id, tempo=tempo, tempo_to=tempo_to, tempo_from=tempo_from, name=name, tag=tag)

List computer audio descriptors

This endpoint lists the descriptors that you can use in the audio regions in an audio render.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: customer_accessCode
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CustomMusicApi(swagger_client.ApiClient(configuration))
render_speed_over = 1.2 # float | Show descriptors with an average render speed that is greater than or equal to the specified value (optional)
band_id = 'band_id_example' # str | Show descriptors that contain the specified band (case-sentsitive) (optional)
band_name = 'band_name_example' # str | Show descriptors with the specified band name (case-sensitive) (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
id = ['id_example'] # list[str] | Show descriptors with the specified IDs (case-sensitive) (optional)
instrument_name = 'instrument_name_example' # str | Show descriptors with the specified instrument name (case-sensitive) (optional)
instrument_id = 'instrument_id_example' # str | Show descriptors with the specified instrument ID (case-sensitive) (optional)
tempo = 1.2 # float | Show descriptors whose tempo range includes the specified tempo in beats per minute (optional)
tempo_to = 1.2 # float | Show descriptors with a tempo that is less than or equal to the specified number (optional)
tempo_from = 1.2 # float | Show descriptors that have a tempo range that includes the specified tempo in beats per minute (optional)
name = 'name_example' # str | Show descriptors with the specified name (case-sensitive) (optional)
tag = 'tag_example' # str | Show descriptors with the specified tag, such as Cinematic or Roomy (case-sensitive) (optional)

try:
    # List computer audio descriptors
    api_response = api_instance.list_custom_descriptors(render_speed_over=render_speed_over, band_id=band_id, band_name=band_name, page=page, per_page=per_page, id=id, instrument_name=instrument_name, instrument_id=instrument_id, tempo=tempo, tempo_to=tempo_to, tempo_from=tempo_from, name=name, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomMusicApi->list_custom_descriptors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **render_speed_over** | **float**| Show descriptors with an average render speed that is greater than or equal to the specified value | [optional] 
 **band_id** | **str**| Show descriptors that contain the specified band (case-sentsitive) | [optional] 
 **band_name** | **str**| Show descriptors with the specified band name (case-sensitive) | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **id** | [**list[str]**](str.md)| Show descriptors with the specified IDs (case-sensitive) | [optional] 
 **instrument_name** | **str**| Show descriptors with the specified instrument name (case-sensitive) | [optional] 
 **instrument_id** | **str**| Show descriptors with the specified instrument ID (case-sensitive) | [optional] 
 **tempo** | **float**| Show descriptors whose tempo range includes the specified tempo in beats per minute | [optional] 
 **tempo_to** | **float**| Show descriptors with a tempo that is less than or equal to the specified number | [optional] 
 **tempo_from** | **float**| Show descriptors that have a tempo range that includes the specified tempo in beats per minute | [optional] 
 **name** | **str**| Show descriptors with the specified name (case-sensitive) | [optional] 
 **tag** | **str**| Show descriptors with the specified tag, such as Cinematic or Roomy (case-sensitive) | [optional] 

### Return type

[**DescriptorsListResult**](DescriptorsListResult.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_instruments**
> InstrumentsListResult list_custom_instruments(id=id, per_page=per_page, page=page, name=name, tag=tag)

List computer audio instruments

This endpoint lists the instruments that you can include in computer audio. If you specify more than one search parameter, the API uses an AND condition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: customer_accessCode
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CustomMusicApi(swagger_client.ApiClient(configuration))
id = ['id_example'] # list[str] | Show instruments with the specified ID (optional)
per_page = 20 # int | Number of results per page (optional) (default to 20)
page = 1 # int | Page number (optional) (default to 1)
name = 'name_example' # str | Show instruments with the specified name (case-sensitive) (optional)
tag = 'tag_example' # str | Show instruments with the specified tag, such as Percussion or Strings (case-sensitive) (optional)

try:
    # List computer audio instruments
    api_response = api_instance.list_custom_instruments(id=id, per_page=per_page, page=page, name=name, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomMusicApi->list_custom_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| Show instruments with the specified ID | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **page** | **int**| Page number | [optional] [default to 1]
 **name** | **str**| Show instruments with the specified name (case-sensitive) | [optional] 
 **tag** | **str**| Show instruments with the specified tag, such as Percussion or Strings (case-sensitive) | [optional] 

### Return type

[**InstrumentsListResult**](InstrumentsListResult.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

