# swagger_client.EditorialImagesApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_editorial_categories**](EditorialImagesApi.md#get_editorial_categories) | **GET** /v2/editorial/categories | (Deprecated) List editorial categories
[**get_editorial_image**](EditorialImagesApi.md#get_editorial_image) | **GET** /v2/editorial/images/{id} | Get editorial content details
[**get_editorial_image_0**](EditorialImagesApi.md#get_editorial_image_0) | **GET** /v2/editorial/{id} | (Deprecated) Get editorial content details
[**get_editorial_image_license_list**](EditorialImagesApi.md#get_editorial_image_license_list) | **GET** /v2/editorial/images/licenses | List editorial image licenses
[**get_editorial_image_livefeed**](EditorialImagesApi.md#get_editorial_image_livefeed) | **GET** /v2/editorial/images/livefeeds/{id} | Get editorial livefeed
[**get_editorial_image_livefeed_items**](EditorialImagesApi.md#get_editorial_image_livefeed_items) | **GET** /v2/editorial/images/livefeeds/{id}/items | Get editorial livefeed items
[**get_editorial_image_livefeed_list**](EditorialImagesApi.md#get_editorial_image_livefeed_list) | **GET** /v2/editorial/images/livefeeds | Get editorial livefeed list
[**get_editorial_livefeed**](EditorialImagesApi.md#get_editorial_livefeed) | **GET** /v2/editorial/livefeeds/{id} | (Deprecated) Get editorial livefeed
[**get_editorial_livefeed_items**](EditorialImagesApi.md#get_editorial_livefeed_items) | **GET** /v2/editorial/livefeeds/{id}/items | (Deprecated) Get editorial livefeed items
[**get_editorial_livefeed_list**](EditorialImagesApi.md#get_editorial_livefeed_list) | **GET** /v2/editorial/livefeeds | (Deprecated) Get editorial livefeed list
[**get_updated_editorial_images**](EditorialImagesApi.md#get_updated_editorial_images) | **GET** /v2/editorial/images/updated | List updated content
[**get_updated_images**](EditorialImagesApi.md#get_updated_images) | **GET** /v2/editorial/updated | (Deprecated) List updated content
[**license_editorial_image**](EditorialImagesApi.md#license_editorial_image) | **POST** /v2/editorial/licenses | (Deprecated) License editorial content
[**license_editorial_images**](EditorialImagesApi.md#license_editorial_images) | **POST** /v2/editorial/images/licenses | License editorial content
[**list_editorial_image_categories**](EditorialImagesApi.md#list_editorial_image_categories) | **GET** /v2/editorial/images/categories | List editorial categories
[**search_editorial**](EditorialImagesApi.md#search_editorial) | **GET** /v2/editorial/search | (Deprecated) Search editorial content
[**search_editorial_images**](EditorialImagesApi.md#search_editorial_images) | **GET** /v2/editorial/images/search | Search editorial images

# **get_editorial_categories**
> EditorialCategoryResults get_editorial_categories()

(Deprecated) List editorial categories

Deprecated; use `GET /v2/editorial/images/categories` instead. This endpoint lists the categories that editorial images can belong to, which are separate from the categories that other types of assets can belong to.

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))

try:
    # (Deprecated) List editorial categories
    api_response = api_instance.get_editorial_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->get_editorial_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EditorialCategoryResults**](EditorialCategoryResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editorial_image**
> EditorialContent get_editorial_image(id, country)

Get editorial content details

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Editorial ID
country = 'country_example' # str | Returns only if the content is available for distribution in a certain country

try:
    # Get editorial content details
    api_response = api_instance.get_editorial_image(id, country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->get_editorial_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Editorial ID | 
 **country** | **str**| Returns only if the content is available for distribution in a certain country | 

### Return type

[**EditorialContent**](EditorialContent.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editorial_image_0**
> EditorialContent get_editorial_image_0(id, country)

(Deprecated) Get editorial content details

Deprecated; use `GET /v2/editorial/images/{id}` instead to show information about an editorial image, including a URL to a preview image and the sizes that it is available in.

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Editorial ID
country = 'country_example' # str | Returns only if the content is available for distribution in a certain country

try:
    # (Deprecated) Get editorial content details
    api_response = api_instance.get_editorial_image_0(id, country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->get_editorial_image_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Editorial ID | 
 **country** | **str**| Returns only if the content is available for distribution in a certain country | 

### Return type

[**EditorialContent**](EditorialContent.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editorial_image_license_list**
> DownloadHistoryDataList get_editorial_image_license_list(image_id=image_id, license=license, page=page, per_page=per_page, sort=sort, username=username, start_date=start_date, end_date=end_date)

List editorial image licenses

This endpoint lists existing editorial image licenses.

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
image_id = 'image_id_example' # str | Show licenses for the specified editorial image ID (optional)
license = 'license_example' # str | Show editorial images that are available with the specified license name (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
sort = 'newest' # str | Sort order (optional) (default to newest)
username = 'username_example' # str | Filter licenses by username of licensee (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Show licenses created on or after the specified date (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Show licenses created before the specified date (optional)

try:
    # List editorial image licenses
    api_response = api_instance.get_editorial_image_license_list(image_id=image_id, license=license, page=page, per_page=per_page, sort=sort, username=username, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->get_editorial_image_license_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| Show licenses for the specified editorial image ID | [optional] 
 **license** | **str**| Show editorial images that are available with the specified license name | [optional] 
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

# **get_editorial_image_livefeed**
> EditorialImageLivefeed get_editorial_image_livefeed(id, country)

Get editorial livefeed

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Editorial livefeed ID; must be an URI encoded string
country = 'country_example' # str | Returns only if the livefeed is available for distribution in a certain country

try:
    # Get editorial livefeed
    api_response = api_instance.get_editorial_image_livefeed(id, country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->get_editorial_image_livefeed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Editorial livefeed ID; must be an URI encoded string | 
 **country** | **str**| Returns only if the livefeed is available for distribution in a certain country | 

### Return type

[**EditorialImageLivefeed**](EditorialImageLivefeed.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editorial_image_livefeed_items**
> EditorialImageContentDataList get_editorial_image_livefeed_items(id, country)

Get editorial livefeed items

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Editorial livefeed ID; must be an URI encoded string
country = 'country_example' # str | Returns only if the livefeed items are available for distribution in a certain country

try:
    # Get editorial livefeed items
    api_response = api_instance.get_editorial_image_livefeed_items(id, country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->get_editorial_image_livefeed_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Editorial livefeed ID; must be an URI encoded string | 
 **country** | **str**| Returns only if the livefeed items are available for distribution in a certain country | 

### Return type

[**EditorialImageContentDataList**](EditorialImageContentDataList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editorial_image_livefeed_list**
> EditorialImageLivefeedList get_editorial_image_livefeed_list(country, page=page, per_page=per_page)

Get editorial livefeed list

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
country = 'country_example' # str | Returns only livefeeds that are available for distribution in a certain country
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)

try:
    # Get editorial livefeed list
    api_response = api_instance.get_editorial_image_livefeed_list(country, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->get_editorial_image_livefeed_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Returns only livefeeds that are available for distribution in a certain country | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 20]

### Return type

[**EditorialImageLivefeedList**](EditorialImageLivefeedList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editorial_livefeed**
> EditorialLivefeed get_editorial_livefeed(id, country)

(Deprecated) Get editorial livefeed

Deprecated: use `GET /v2/editorial/images/livefeeds/{id}` instead to get an editorial livefeed.

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Editorial livefeed ID; must be an URI encoded string
country = 'country_example' # str | Returns only if the livefeed is available for distribution in a certain country

try:
    # (Deprecated) Get editorial livefeed
    api_response = api_instance.get_editorial_livefeed(id, country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->get_editorial_livefeed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Editorial livefeed ID; must be an URI encoded string | 
 **country** | **str**| Returns only if the livefeed is available for distribution in a certain country | 

### Return type

[**EditorialLivefeed**](EditorialLivefeed.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editorial_livefeed_items**
> EditorialContentDataList get_editorial_livefeed_items(id, country)

(Deprecated) Get editorial livefeed items

Deprecated; use `GET /v2/editorial/images/livefeeds/{id}/items` instead to get editorial livefeed items.

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Editorial livefeed ID; must be an URI encoded string
country = 'country_example' # str | Returns only if the livefeed items are available for distribution in a certain country

try:
    # (Deprecated) Get editorial livefeed items
    api_response = api_instance.get_editorial_livefeed_items(id, country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->get_editorial_livefeed_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Editorial livefeed ID; must be an URI encoded string | 
 **country** | **str**| Returns only if the livefeed items are available for distribution in a certain country | 

### Return type

[**EditorialContentDataList**](EditorialContentDataList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editorial_livefeed_list**
> EditorialLivefeedList get_editorial_livefeed_list(country, page=page, per_page=per_page)

(Deprecated) Get editorial livefeed list

Deprecated; use `GET /v2/editorial/images/livefeeds` instead to get a list of editorial livefeeds.

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
country = 'country_example' # str | Returns only livefeeds that are available for distribution in a certain country
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)

try:
    # (Deprecated) Get editorial livefeed list
    api_response = api_instance.get_editorial_livefeed_list(country, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->get_editorial_livefeed_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Returns only livefeeds that are available for distribution in a certain country | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 20]

### Return type

[**EditorialLivefeedList**](EditorialLivefeedList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_updated_editorial_images**
> EditorialUpdatedResults get_updated_editorial_images(type, date_updated_start, date_updated_end, country, date_taken_start=date_taken_start, date_taken_end=date_taken_end, cursor=cursor, sort=sort, supplier_code=supplier_code, per_page=per_page)

List updated content

This endpoint lists editorial images that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the date_updated_start and date_updated_end parameters to specify a range updates based on when the updates happened. You can also use the date_taken_start and date_taken_end parameters to specify a range of updates based on when the image was taken.

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Specify `addition` to return only images that were added or `edit` to return only images that were edited or deleted
date_updated_start = '2013-10-20T19:20:30+01:00' # datetime | Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
date_updated_end = '2013-10-20T19:20:30+01:00' # datetime | Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
country = 'country_example' # str | Show only editorial content that is available for distribution in a certain country
date_taken_start = 'date_taken_start_example' # str | Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets (optional)
date_taken_end = 'date_taken_end_example' # str | Show images that were taken before the specified date (optional)
cursor = 'cursor_example' # str | The cursor of the page with which to start fetching results; this cursor is returned from previous requests (optional)
sort = 'newest' # str | Sort by (optional) (default to newest)
supplier_code = ['supplier_code_example'] # list[str] | Show only editorial content from certain suppliers (optional)
per_page = 500 # int | Number of results per page (optional) (default to 500)

try:
    # List updated content
    api_response = api_instance.get_updated_editorial_images(type, date_updated_start, date_updated_end, country, date_taken_start=date_taken_start, date_taken_end=date_taken_end, cursor=cursor, sort=sort, supplier_code=supplier_code, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->get_updated_editorial_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Specify &#x60;addition&#x60; to return only images that were added or &#x60;edit&#x60; to return only images that were edited or deleted | 
 **date_updated_start** | **datetime**| Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. | 
 **date_updated_end** | **datetime**| Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. | 
 **country** | **str**| Show only editorial content that is available for distribution in a certain country | 
 **date_taken_start** | **str**| Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets | [optional] 
 **date_taken_end** | **str**| Show images that were taken before the specified date | [optional] 
 **cursor** | **str**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] 
 **sort** | **str**| Sort by | [optional] [default to newest]
 **supplier_code** | [**list[str]**](str.md)| Show only editorial content from certain suppliers | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 500]

### Return type

[**EditorialUpdatedResults**](EditorialUpdatedResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_updated_images**
> EditorialUpdatedResults get_updated_images(type, date_updated_start, date_updated_end, country, date_taken_start=date_taken_start, date_taken_end=date_taken_end, cursor=cursor, sort=sort, supplier_code=supplier_code, per_page=per_page)

(Deprecated) List updated content

Deprecated; use `GET /v2/editorial/images/updated` instead to get recently updated items.

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Specify `addition` to return only images that were added or `edit` to return only images that were edited or deleted
date_updated_start = '2013-10-20T19:20:30+01:00' # datetime | Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
date_updated_end = '2013-10-20T19:20:30+01:00' # datetime | Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
country = 'country_example' # str | Show only editorial content that is available for distribution in a certain country
date_taken_start = 'date_taken_start_example' # str | Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets (optional)
date_taken_end = 'date_taken_end_example' # str | Show images that were taken before the specified date (optional)
cursor = 'cursor_example' # str | The cursor of the page with which to start fetching results; this cursor is returned from previous requests (optional)
sort = 'newest' # str | Sort by (optional) (default to newest)
supplier_code = ['supplier_code_example'] # list[str] | Show only editorial content from certain suppliers (optional)
per_page = 500 # int | Number of results per page (optional) (default to 500)

try:
    # (Deprecated) List updated content
    api_response = api_instance.get_updated_images(type, date_updated_start, date_updated_end, country, date_taken_start=date_taken_start, date_taken_end=date_taken_end, cursor=cursor, sort=sort, supplier_code=supplier_code, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->get_updated_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Specify &#x60;addition&#x60; to return only images that were added or &#x60;edit&#x60; to return only images that were edited or deleted | 
 **date_updated_start** | **datetime**| Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. | 
 **date_updated_end** | **datetime**| Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. | 
 **country** | **str**| Show only editorial content that is available for distribution in a certain country | 
 **date_taken_start** | **str**| Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets | [optional] 
 **date_taken_end** | **str**| Show images that were taken before the specified date | [optional] 
 **cursor** | **str**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] 
 **sort** | **str**| Sort by | [optional] [default to newest]
 **supplier_code** | [**list[str]**](str.md)| Show only editorial content from certain suppliers | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 500]

### Return type

[**EditorialUpdatedResults**](EditorialUpdatedResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_editorial_image**
> LicenseEditorialContentResults license_editorial_image(body)

(Deprecated) License editorial content

Deprecated; use `POST /v2/editorial/images/licenses` instead to get licenses for one or more editorial images. You must specify the country and one or more editorial images to license.

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
body = swagger_client.LicenseEditorialContentRequest() # LicenseEditorialContentRequest | License editorial content

try:
    # (Deprecated) License editorial content
    api_response = api_instance.license_editorial_image(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->license_editorial_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LicenseEditorialContentRequest**](LicenseEditorialContentRequest.md)| License editorial content | 

### Return type

[**LicenseEditorialContentResults**](LicenseEditorialContentResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_editorial_images**
> LicenseEditorialContentResults license_editorial_images(body)

License editorial content

This endpoint gets licenses for one or more editorial images. You must specify the country and one or more editorial images to license.

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
body = swagger_client.LicenseEditorialContentRequest() # LicenseEditorialContentRequest | License editorial content

try:
    # License editorial content
    api_response = api_instance.license_editorial_images(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->license_editorial_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LicenseEditorialContentRequest**](LicenseEditorialContentRequest.md)| License editorial content | 

### Return type

[**LicenseEditorialContentResults**](LicenseEditorialContentResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_editorial_image_categories**
> EditorialImageCategoryResults list_editorial_image_categories()

List editorial categories

This endpoint lists the categories that editorial images can belong to, which are separate from the categories that other types of assets can belong to.

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))

try:
    # List editorial categories
    api_response = api_instance.list_editorial_image_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->list_editorial_image_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EditorialImageCategoryResults**](EditorialImageCategoryResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_editorial**
> EditorialSearchResults search_editorial(country, query=query, sort=sort, category=category, supplier_code=supplier_code, date_start=date_start, date_end=date_end, per_page=per_page, cursor=cursor)

(Deprecated) Search editorial content

Deprecated; use `GET /v2/editorial/images/search` instead to search for editorial images.

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
country = 'country_example' # str | Show only editorial content that is available for distribution in a certain country
query = 'query_example' # str | One or more search terms separated by spaces (optional)
sort = 'relevant' # str | Sort by (optional) (default to relevant)
category = 'category_example' # str | Show editorial content within a certain editorial category; specify by category name (optional)
supplier_code = ['supplier_code_example'] # list[str] | Show only editorial content from certain suppliers (optional)
date_start = '2013-10-20' # date | Show only editorial content generated on or after a specific date (optional)
date_end = '2013-10-20' # date | Show only editorial content generated on or before a specific date (optional)
per_page = 20 # int | Number of results per page (optional) (default to 20)
cursor = 'cursor_example' # str | The cursor of the page with which to start fetching results; this cursor is returned from previous requests (optional)

try:
    # (Deprecated) Search editorial content
    api_response = api_instance.search_editorial(country, query=query, sort=sort, category=category, supplier_code=supplier_code, date_start=date_start, date_end=date_end, per_page=per_page, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->search_editorial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Show only editorial content that is available for distribution in a certain country | 
 **query** | **str**| One or more search terms separated by spaces | [optional] 
 **sort** | **str**| Sort by | [optional] [default to relevant]
 **category** | **str**| Show editorial content within a certain editorial category; specify by category name | [optional] 
 **supplier_code** | [**list[str]**](str.md)| Show only editorial content from certain suppliers | [optional] 
 **date_start** | **date**| Show only editorial content generated on or after a specific date | [optional] 
 **date_end** | **date**| Show only editorial content generated on or before a specific date | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **cursor** | **str**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] 

### Return type

[**EditorialSearchResults**](EditorialSearchResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_editorial_images**
> EditorialSearchResults search_editorial_images(country, query=query, sort=sort, category=category, supplier_code=supplier_code, date_start=date_start, date_end=date_end, per_page=per_page, cursor=cursor)

Search editorial images

This endpoint searches for editorial images. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the `query` parameter by prefixing the term with NOT.

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
api_instance = swagger_client.EditorialImagesApi(swagger_client.ApiClient(configuration))
country = 'country_example' # str | Show only editorial content that is available for distribution in a certain country
query = 'query_example' # str | One or more search terms separated by spaces (optional)
sort = 'relevant' # str | Sort by (optional) (default to relevant)
category = 'category_example' # str | Show editorial content within a certain editorial category; specify by category name (optional)
supplier_code = ['supplier_code_example'] # list[str] | Show only editorial content from certain suppliers (optional)
date_start = '2013-10-20' # date | Show only editorial content generated on or after a specific date (optional)
date_end = '2013-10-20' # date | Show only editorial content generated on or before a specific date (optional)
per_page = 20 # int | Number of results per page (optional) (default to 20)
cursor = 'cursor_example' # str | The cursor of the page with which to start fetching results; this cursor is returned from previous requests (optional)

try:
    # Search editorial images
    api_response = api_instance.search_editorial_images(country, query=query, sort=sort, category=category, supplier_code=supplier_code, date_start=date_start, date_end=date_end, per_page=per_page, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialImagesApi->search_editorial_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Show only editorial content that is available for distribution in a certain country | 
 **query** | **str**| One or more search terms separated by spaces | [optional] 
 **sort** | **str**| Sort by | [optional] [default to relevant]
 **category** | **str**| Show editorial content within a certain editorial category; specify by category name | [optional] 
 **supplier_code** | [**list[str]**](str.md)| Show only editorial content from certain suppliers | [optional] 
 **date_start** | **date**| Show only editorial content generated on or after a specific date | [optional] 
 **date_end** | **date**| Show only editorial content generated on or before a specific date | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **cursor** | **str**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] 

### Return type

[**EditorialSearchResults**](EditorialSearchResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

