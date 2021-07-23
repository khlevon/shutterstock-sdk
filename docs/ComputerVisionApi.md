# shutterstock_sdk.ComputerVisionApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_keywords**](ComputerVisionApi.md#get_keywords) | **GET** /v2/cv/keywords | List suggested keywords
[**get_similar_images**](ComputerVisionApi.md#get_similar_images) | **GET** /v2/cv/similar/images | List similar images
[**get_similar_videos**](ComputerVisionApi.md#get_similar_videos) | **GET** /v2/cv/similar/videos | List similar videos
[**upload_ephemeral_image**](ComputerVisionApi.md#upload_ephemeral_image) | **POST** /v2/images | Upload ephemeral images
[**upload_image**](ComputerVisionApi.md#upload_image) | **POST** /v2/cv/images | Upload images

# **get_keywords**
> KeywordDataList get_keywords(asset_id)

List suggested keywords

This endpoint returns a list of suggested keywords for a media item that you specify or upload.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = shutterstock_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ComputerVisionApi(shutterstock_sdk.ApiClient(configuration))
asset_id = shutterstock_sdk.AssetId() # AssetId | The asset ID or upload ID to suggest keywords for

try:
    # List suggested keywords
    api_response = api_instance.get_keywords(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputerVisionApi->get_keywords: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**AssetId**](.md)| The asset ID or upload ID to suggest keywords for | 

### Return type

[**KeywordDataList**](KeywordDataList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_similar_images**
> ImageSearchResults get_similar_images(asset_id, license=license, safe=safe, language=language, page=page, per_page=per_page, view=view)

List similar images

This endpoint returns images that are visually similar to an image that you specify or upload.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = shutterstock_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ComputerVisionApi(shutterstock_sdk.ApiClient(configuration))
asset_id = 'asset_id_example' # str | The asset ID or upload ID to find similar images for
license = ['license_example'] # list[str] | Show only images with the specified license (optional)
safe = true # bool | Enable or disable safe search (optional) (default to true)
language = shutterstock_sdk.Language() # Language | Language for the keywords and categories in the response (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
view = 'minimal' # str | Amount of detail to render in the response (optional) (default to minimal)

try:
    # List similar images
    api_response = api_instance.get_similar_images(asset_id, license=license, safe=safe, language=language, page=page, per_page=per_page, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputerVisionApi->get_similar_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID or upload ID to find similar images for | 
 **license** | [**list[str]**](str.md)| Show only images with the specified license | [optional] 
 **safe** | **bool**| Enable or disable safe search | [optional] [default to true]
 **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **view** | **str**| Amount of detail to render in the response | [optional] [default to minimal]

### Return type

[**ImageSearchResults**](ImageSearchResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_similar_videos**
> VideoSearchResults get_similar_videos(asset_id, license=license, safe=safe, language=language, page=page, per_page=per_page, view=view)

List similar videos

This endpoint returns videos that are visually similar to an image that you specify or upload.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = shutterstock_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ComputerVisionApi(shutterstock_sdk.ApiClient(configuration))
asset_id = 'asset_id_example' # str | The asset ID or upload ID to find similar videos for
license = ['license_example'] # list[str] | Show only videos with the specified license (optional)
safe = true # bool | Enable or disable safe search (optional) (default to true)
language = shutterstock_sdk.Language() # Language | Language for the keywords and categories in the response (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
view = 'minimal' # str | Amount of detail to render in the response (optional) (default to minimal)

try:
    # List similar videos
    api_response = api_instance.get_similar_videos(asset_id, license=license, safe=safe, language=language, page=page, per_page=per_page, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputerVisionApi->get_similar_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID or upload ID to find similar videos for | 
 **license** | [**list[str]**](str.md)| Show only videos with the specified license | [optional] 
 **safe** | **bool**| Enable or disable safe search | [optional] [default to true]
 **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **view** | **str**| Amount of detail to render in the response | [optional] [default to minimal]

### Return type

[**VideoSearchResults**](VideoSearchResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_ephemeral_image**
> ImageCreateResponse upload_ephemeral_image(body)

Upload ephemeral images

Deprecated; use `POST /v2/cv/images` instead. This endpoint uploads an image for reverse image search. The image must be in JPEG or PNG format. To get the search results, pass the ID that this endpoint returns to the `GET /v2/images/{id}/similar` endpoint.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = shutterstock_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ComputerVisionApi(shutterstock_sdk.ApiClient(configuration))
body = shutterstock_sdk.ImageCreateRequest() # ImageCreateRequest | The image data in JPEG or PNG format

try:
    # Upload ephemeral images
    api_response = api_instance.upload_ephemeral_image(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputerVisionApi->upload_ephemeral_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageCreateRequest**](ImageCreateRequest.md)| The image data in JPEG or PNG format | 

### Return type

[**ImageCreateResponse**](ImageCreateResponse.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_image**
> ComputerVisionImageCreateResponse upload_image(body)

Upload images

This endpoint uploads an image for reverse image or video search. Images must be in JPEG or PNG format. To get the search results, pass the upload ID that this endpoint returns to the GET /v2/cv/similar/images or GET /v2/cv/similar/videos endpoints. Contact us for access to this endpoint.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = shutterstock_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ComputerVisionApi(shutterstock_sdk.ApiClient(configuration))
body = shutterstock_sdk.ImageCreateRequest() # ImageCreateRequest | A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width or height

try:
    # Upload images
    api_response = api_instance.upload_image(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputerVisionApi->upload_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageCreateRequest**](ImageCreateRequest.md)| A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width or height | 

### Return type

[**ComputerVisionImageCreateResponse**](ComputerVisionImageCreateResponse.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

