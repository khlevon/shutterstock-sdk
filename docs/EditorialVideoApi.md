# swagger_client.EditorialVideoApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_editorial_video**](EditorialVideoApi.md#get_editorial_video) | **GET** /v2/editorial/videos/{id} | Get editorial video content details
[**get_editorial_video_license_list**](EditorialVideoApi.md#get_editorial_video_license_list) | **GET** /v2/editorial/videos/licenses | List editorial video licenses
[**license_editorial_video**](EditorialVideoApi.md#license_editorial_video) | **POST** /v2/editorial/videos/licenses | License editorial video content
[**list_editorial_video_categories**](EditorialVideoApi.md#list_editorial_video_categories) | **GET** /v2/editorial/videos/categories | List editorial video categories
[**search_editorial_videos**](EditorialVideoApi.md#search_editorial_videos) | **GET** /v2/editorial/videos/search | Search editorial video content

# **get_editorial_video**
> EditorialVideoContent get_editorial_video(id, country)

Get editorial video content details

This endpoint shows information about an editorial image, including a URL to a preview image and the sizes that it is available in.

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
api_instance = swagger_client.EditorialVideoApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Editorial ID
country = 'country_example' # str | Returns only if the content is available for distribution in a certain country

try:
    # Get editorial video content details
    api_response = api_instance.get_editorial_video(id, country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialVideoApi->get_editorial_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Editorial ID | 
 **country** | **str**| Returns only if the content is available for distribution in a certain country | 

### Return type

[**EditorialVideoContent**](EditorialVideoContent.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editorial_video_license_list**
> DownloadHistoryDataList get_editorial_video_license_list(video_id=video_id, license=license, page=page, per_page=per_page, sort=sort, username=username, start_date=start_date, end_date=end_date)

List editorial video licenses

This endpoint lists existing editorial video licenses.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.EditorialVideoApi(swagger_client.ApiClient(configuration))
video_id = 'video_id_example' # str | Show licenses for the specified editorial video ID (optional)
license = 'license_example' # str | Show editorial videos that are available with the specified license name (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
sort = 'newest' # str | Sort order (optional) (default to newest)
username = 'username_example' # str | Filter licenses by username of licensee (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Show licenses created on or after the specified date (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Show licenses created before the specified date (optional)

try:
    # List editorial video licenses
    api_response = api_instance.get_editorial_video_license_list(video_id=video_id, license=license, page=page, per_page=per_page, sort=sort, username=username, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialVideoApi->get_editorial_video_license_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Show licenses for the specified editorial video ID | [optional] 
 **license** | **str**| Show editorial videos that are available with the specified license name | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **sort** | **str**| Sort order | [optional] [default to newest]
 **username** | **str**| Filter licenses by username of licensee | [optional] 
 **start_date** | **datetime**| Show licenses created on or after the specified date | [optional] 
 **end_date** | **datetime**| Show licenses created before the specified date | [optional] 

### Return type

[**DownloadHistoryDataList**](DownloadHistoryDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_editorial_video**
> LicenseEditorialContentResults license_editorial_video(body)

License editorial video content

This endpoint gets licenses for one or more editorial videos. You must specify the country and one or more editorial videos to license.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.EditorialVideoApi(swagger_client.ApiClient(configuration))
body = swagger_client.LicenseEditorialVideoContentRequest() # LicenseEditorialVideoContentRequest | License editorial video content

try:
    # License editorial video content
    api_response = api_instance.license_editorial_video(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialVideoApi->license_editorial_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LicenseEditorialVideoContentRequest**](LicenseEditorialVideoContentRequest.md)| License editorial video content | 

### Return type

[**LicenseEditorialContentResults**](LicenseEditorialContentResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_editorial_video_categories**
> EditorialVideoCategoryResults list_editorial_video_categories()

List editorial video categories

This endpoint lists the categories that editorial videos can belong to, which are separate from the categories that other types of assets can belong to.

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
api_instance = swagger_client.EditorialVideoApi(swagger_client.ApiClient(configuration))

try:
    # List editorial video categories
    api_response = api_instance.list_editorial_video_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialVideoApi->list_editorial_video_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EditorialVideoCategoryResults**](EditorialVideoCategoryResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_editorial_videos**
> EditorialVideoSearchResults search_editorial_videos(country, query=query, sort=sort, category=category, supplier_code=supplier_code, date_start=date_start, date_end=date_end, resolution=resolution, fps=fps, per_page=per_page, cursor=cursor)

Search editorial video content

This endpoint searches for editorial videos. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the `query` parameter by prefixing the term with NOT.

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
api_instance = swagger_client.EditorialVideoApi(swagger_client.ApiClient(configuration))
country = 'country_example' # str | Show only editorial video content that is available for distribution in a certain country
query = 'query_example' # str | One or more search terms separated by spaces (optional)
sort = 'relevant' # str | Sort by (optional) (default to relevant)
category = 'category_example' # str | Show editorial video content within a certain editorial category; specify by category name (optional)
supplier_code = ['supplier_code_example'] # list[str] | Show only editorial video content from certain suppliers (optional)
date_start = '2013-10-20' # date | Show only editorial video content generated on or after a specific date (optional)
date_end = '2013-10-20' # date | Show only editorial video content generated on or before a specific date (optional)
resolution = 'resolution_example' # str | Show only editorial video content with specific resolution (optional)
fps = 1.2 # float | Show only editorial video content generated with specific frames per second (optional)
per_page = 20 # int | Number of results per page (optional) (default to 20)
cursor = 'cursor_example' # str | The cursor of the page with which to start fetching results; this cursor is returned from previous requests (optional)

try:
    # Search editorial video content
    api_response = api_instance.search_editorial_videos(country, query=query, sort=sort, category=category, supplier_code=supplier_code, date_start=date_start, date_end=date_end, resolution=resolution, fps=fps, per_page=per_page, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialVideoApi->search_editorial_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Show only editorial video content that is available for distribution in a certain country | 
 **query** | **str**| One or more search terms separated by spaces | [optional] 
 **sort** | **str**| Sort by | [optional] [default to relevant]
 **category** | **str**| Show editorial video content within a certain editorial category; specify by category name | [optional] 
 **supplier_code** | [**list[str]**](str.md)| Show only editorial video content from certain suppliers | [optional] 
 **date_start** | **date**| Show only editorial video content generated on or after a specific date | [optional] 
 **date_end** | **date**| Show only editorial video content generated on or before a specific date | [optional] 
 **resolution** | **str**| Show only editorial video content with specific resolution | [optional] 
 **fps** | **float**| Show only editorial video content generated with specific frames per second | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **cursor** | **str**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] 

### Return type

[**EditorialVideoSearchResults**](EditorialVideoSearchResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

