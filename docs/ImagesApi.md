# shutterstock_sdk.ImagesApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_image_collection_items**](ImagesApi.md#add_image_collection_items) | **POST** /v2/images/collections/{id}/items | Add images to collections
[**create_image_collection**](ImagesApi.md#create_image_collection) | **POST** /v2/images/collections | Create image collections
[**delete_image_collection**](ImagesApi.md#delete_image_collection) | **DELETE** /v2/images/collections/{id} | Delete image collections
[**delete_image_collection_items**](ImagesApi.md#delete_image_collection_items) | **DELETE** /v2/images/collections/{id}/items | Remove images from collections
[**download_image**](ImagesApi.md#download_image) | **POST** /v2/images/licenses/{id}/downloads | Download images
[**get_featured_image_collection**](ImagesApi.md#get_featured_image_collection) | **GET** /v2/images/collections/featured/{id} | Get the details of featured image collections
[**get_featured_image_collection_items**](ImagesApi.md#get_featured_image_collection_items) | **GET** /v2/images/collections/featured/{id}/items | Get the contents of featured image collections
[**get_featured_image_collection_list**](ImagesApi.md#get_featured_image_collection_list) | **GET** /v2/images/collections/featured | List featured image collections
[**get_image**](ImagesApi.md#get_image) | **GET** /v2/images/{id} | Get details about images
[**get_image_collection**](ImagesApi.md#get_image_collection) | **GET** /v2/images/collections/{id} | Get the details of image collections
[**get_image_collection_items**](ImagesApi.md#get_image_collection_items) | **GET** /v2/images/collections/{id}/items | Get the contents of image collections
[**get_image_collection_list**](ImagesApi.md#get_image_collection_list) | **GET** /v2/images/collections | List image collections
[**get_image_keyword_suggestions**](ImagesApi.md#get_image_keyword_suggestions) | **POST** /v2/images/search/suggestions | Get keywords from text
[**get_image_license_list**](ImagesApi.md#get_image_license_list) | **GET** /v2/images/licenses | List image licenses
[**get_image_list**](ImagesApi.md#get_image_list) | **GET** /v2/images | List images
[**get_image_recommendations**](ImagesApi.md#get_image_recommendations) | **GET** /v2/images/recommendations | List recommended images
[**get_image_suggestions**](ImagesApi.md#get_image_suggestions) | **GET** /v2/images/search/suggestions | Get suggestions for a search term
[**get_similar_images**](ImagesApi.md#get_similar_images) | **GET** /v2/images/{id}/similar | List similar images
[**get_updated_images**](ImagesApi.md#get_updated_images) | **GET** /v2/images/updated | List updated images
[**license_images**](ImagesApi.md#license_images) | **POST** /v2/images/licenses | License images
[**list_image_categories**](ImagesApi.md#list_image_categories) | **GET** /v2/images/categories | List image categories
[**rename_image_collection**](ImagesApi.md#rename_image_collection) | **POST** /v2/images/collections/{id} | Rename image collections
[**search_images**](ImagesApi.md#search_images) | **GET** /v2/images/search | Search for images

# **add_image_collection_items**
> add_image_collection_items(body, id)

Add images to collections

This endpoint adds one or more images to a collection by image IDs.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
body = shutterstock_sdk.CollectionItemRequest() # CollectionItemRequest | Array of image IDs to add to the collection
id = 'id_example' # str | Collection ID

try:
    # Add images to collections
    api_instance.add_image_collection_items(body, id)
except ApiException as e:
    print("Exception when calling ImagesApi->add_image_collection_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionItemRequest**](CollectionItemRequest.md)| Array of image IDs to add to the collection | 
 **id** | **str**| Collection ID | 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_collection**
> CollectionCreateResponse create_image_collection(body)

Create image collections

This endpoint creates one or more image collections (lightboxes). To add images to the collections, use `POST /v2/images/collections/{id}/items`.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
body = shutterstock_sdk.CollectionCreateRequest() # CollectionCreateRequest | The names of the new collections

try:
    # Create image collections
    api_response = api_instance.create_image_collection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->create_image_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionCreateRequest**](CollectionCreateRequest.md)| The names of the new collections | 

### Return type

[**CollectionCreateResponse**](CollectionCreateResponse.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image_collection**
> delete_image_collection(id)

Delete image collections

This endpoint deletes an image collection.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
id = 'id_example' # str | Collection ID

try:
    # Delete image collections
    api_instance.delete_image_collection(id)
except ApiException as e:
    print("Exception when calling ImagesApi->delete_image_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image_collection_items**
> delete_image_collection_items(id, item_id=item_id)

Remove images from collections

This endpoint removes one or more images from a collection.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
id = 'id_example' # str | Collection ID
item_id = ['item_id_example'] # list[str] | One or more image IDs to remove from the collection (optional)

try:
    # Remove images from collections
    api_instance.delete_image_collection_items(id, item_id=item_id)
except ApiException as e:
    print("Exception when calling ImagesApi->delete_image_collection_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **item_id** | [**list[str]**](str.md)| One or more image IDs to remove from the collection | [optional] 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_image**
> Url download_image(body, id)

Download images

This endpoint redownloads images that you have already received a license for.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
body = shutterstock_sdk.RedownloadImage() # RedownloadImage | Information about the images to redownload
id = 'id_example' # str | License ID

try:
    # Download images
    api_response = api_instance.download_image(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->download_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RedownloadImage**](RedownloadImage.md)| Information about the images to redownload | 
 **id** | **str**| License ID | 

### Return type

[**Url**](Url.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featured_image_collection**
> FeaturedCollection get_featured_image_collection(id, embed=embed, asset_hint=asset_hint)

Get the details of featured image collections

This endpoint gets more detailed information about a featured collection, including its cover image and timestamps for its creation and most recent update. To get the images, use `GET /v2/images/collections/featured/{id}/items`.

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
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
id = 'id_example' # str | Collection ID
embed = 'embed_example' # str | Which sharing information to include in the response, such as a URL to the collection (optional)
asset_hint = '1x' # str | Cover image size (optional) (default to 1x)

try:
    # Get the details of featured image collections
    api_response = api_instance.get_featured_image_collection(id, embed=embed, asset_hint=asset_hint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_featured_image_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **embed** | **str**| Which sharing information to include in the response, such as a URL to the collection | [optional] 
 **asset_hint** | **str**| Cover image size | [optional] [default to 1x]

### Return type

[**FeaturedCollection**](FeaturedCollection.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featured_image_collection_items**
> CollectionItemDataList get_featured_image_collection_items(id, page=page, per_page=per_page)

Get the contents of featured image collections

This endpoint lists the IDs of images in a featured collection and the date that each was added.

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
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
id = 'id_example' # str | Collection ID
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Number of results per page (optional) (default to 100)

try:
    # Get the contents of featured image collections
    api_response = api_instance.get_featured_image_collection_items(id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_featured_image_collection_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 100]

### Return type

[**CollectionItemDataList**](CollectionItemDataList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featured_image_collection_list**
> FeaturedCollectionDataList get_featured_image_collection_list(embed=embed, type=type, asset_hint=asset_hint)

List featured image collections

This endpoint lists featured collections of specific types and a name and cover image for each collection.

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
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
embed = 'embed_example' # str | Which sharing information to include in the response, such as a URL to the collection (optional)
type = ['type_example'] # list[str] | The types of collections to return (optional)
asset_hint = '1x' # str | Cover image size (optional) (default to 1x)

try:
    # List featured image collections
    api_response = api_instance.get_featured_image_collection_list(embed=embed, type=type, asset_hint=asset_hint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_featured_image_collection_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embed** | **str**| Which sharing information to include in the response, such as a URL to the collection | [optional] 
 **type** | [**list[str]**](str.md)| The types of collections to return | [optional] 
 **asset_hint** | **str**| Cover image size | [optional] [default to 1x]

### Return type

[**FeaturedCollectionDataList**](FeaturedCollectionDataList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image**
> Image get_image(id, language=language, view=view)

Get details about images

This endpoint shows information about an image, including a URL to a preview image and the sizes that it is available in.

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
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
id = 'id_example' # str | Image ID
language = shutterstock_sdk.Language() # Language | Language for the keywords and categories in the response (optional)
view = 'full' # str | Amount of detail to render in the response (optional) (default to full)

try:
    # Get details about images
    api_response = api_instance.get_image(id, language=language, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Image ID | 
 **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] 
 **view** | **str**| Amount of detail to render in the response | [optional] [default to full]

### Return type

[**Image**](Image.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_collection**
> Collection get_image_collection(id, embed=embed, share_code=share_code)

Get the details of image collections

This endpoint gets more detailed information about a collection, including its cover image and timestamps for its creation and most recent update. To get the images in collections, use `GET /v2/images/collections/{id}/items`.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
id = 'id_example' # str | Collection ID
embed = ['embed_example'] # list[str] | Which sharing information to include in the response, such as a URL to the collection (optional)
share_code = 'share_code_example' # str | Code to retrieve a shared collection (optional)

try:
    # Get the details of image collections
    api_response = api_instance.get_image_collection(id, embed=embed, share_code=share_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **embed** | [**list[str]**](str.md)| Which sharing information to include in the response, such as a URL to the collection | [optional] 
 **share_code** | **str**| Code to retrieve a shared collection | [optional] 

### Return type

[**Collection**](Collection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_collection_items**
> CollectionItemDataList get_image_collection_items(id, share_code=share_code, page=page, per_page=per_page)

Get the contents of image collections

This endpoint lists the IDs of images in a collection and the date that each was added.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
id = 'id_example' # str | Collection ID
share_code = 'share_code_example' # str | Code to retrieve the contents of a shared collection (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Number of results per page (optional) (default to 100)

try:
    # Get the contents of image collections
    api_response = api_instance.get_image_collection_items(id, share_code=share_code, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_collection_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **share_code** | **str**| Code to retrieve the contents of a shared collection | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 100]

### Return type

[**CollectionItemDataList**](CollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_collection_list**
> CollectionDataList get_image_collection_list(embed=embed, page=page, per_page=per_page)

List image collections

This endpoint lists your collections of images and their basic attributes.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
embed = ['embed_example'] # list[str] | Which sharing information to include in the response, such as a URL to the collection (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Number of results per page (optional) (default to 100)

try:
    # List image collections
    api_response = api_instance.get_image_collection_list(embed=embed, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_collection_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embed** | [**list[str]**](str.md)| Which sharing information to include in the response, such as a URL to the collection | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 100]

### Return type

[**CollectionDataList**](CollectionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_keyword_suggestions**
> SearchEntitiesResponse get_image_keyword_suggestions(body)

Get keywords from text

This endpoint returns up to 10 important keywords from a block of plain text.

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
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
body = shutterstock_sdk.SearchEntitiesRequest() # SearchEntitiesRequest | Plain text to extract keywords from

try:
    # Get keywords from text
    api_response = api_instance.get_image_keyword_suggestions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_keyword_suggestions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchEntitiesRequest**](SearchEntitiesRequest.md)| Plain text to extract keywords from | 

### Return type

[**SearchEntitiesResponse**](SearchEntitiesResponse.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_license_list**
> DownloadHistoryDataList get_image_license_list(image_id=image_id, license=license, page=page, per_page=per_page, sort=sort, username=username, start_date=start_date, end_date=end_date)

List image licenses

This endpoint lists existing licenses.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
image_id = 'image_id_example' # str | Show licenses for the specified image ID (optional)
license = 'license_example' # str | Show images that are available with the specified license, such as `standard` or `enhanced`; prepending a `-` sign excludes results from that license (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
sort = 'newest' # str | Sort order (optional) (default to newest)
username = 'username_example' # str | Filter licenses by username of licensee (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Show licenses created on or after the specified date (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Show licenses created before the specified date (optional)

try:
    # List image licenses
    api_response = api_instance.get_image_license_list(image_id=image_id, license=license, page=page, per_page=per_page, sort=sort, username=username, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_license_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| Show licenses for the specified image ID | [optional] 
 **license** | **str**| Show images that are available with the specified license, such as &#x60;standard&#x60; or &#x60;enhanced&#x60;; prepending a &#x60;-&#x60; sign excludes results from that license | [optional] 
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

# **get_image_list**
> ImageDataList get_image_list(id, view=view)

List images

This endpoint lists information about one or more images, including the available sizes.

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
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
id = ['id_example'] # list[str] | One or more image IDs
view = 'minimal' # str | Amount of detail to render in the response (optional) (default to minimal)

try:
    # List images
    api_response = api_instance.get_image_list(id, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| One or more image IDs | 
 **view** | **str**| Amount of detail to render in the response | [optional] [default to minimal]

### Return type

[**ImageDataList**](ImageDataList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_recommendations**
> RecommendationDataList get_image_recommendations(id, max_items=max_items, safe=safe)

List recommended images

This endpoint returns images that customers put in the same collection as the specified image IDs.

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
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
id = ['id_example'] # list[str] | Image IDs
max_items = 20 # int | Maximum number of results returned in the response (optional) (default to 20)
safe = true # bool | Restrict results to safe images (optional) (default to true)

try:
    # List recommended images
    api_response = api_instance.get_image_recommendations(id, max_items=max_items, safe=safe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_recommendations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| Image IDs | 
 **max_items** | **int**| Maximum number of results returned in the response | [optional] [default to 20]
 **safe** | **bool**| Restrict results to safe images | [optional] [default to true]

### Return type

[**RecommendationDataList**](RecommendationDataList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_suggestions**
> Suggestions get_image_suggestions(query, limit=limit)

Get suggestions for a search term

This endpoint provides autocomplete suggestions for partial search terms.

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
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
query = 'query_example' # str | Search term for which you want keyword suggestions
limit = 10 # int | Limit the number of suggestions (optional) (default to 10)

try:
    # Get suggestions for a search term
    api_response = api_instance.get_image_suggestions(query, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_suggestions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search term for which you want keyword suggestions | 
 **limit** | **int**| Limit the number of suggestions | [optional] [default to 10]

### Return type

[**Suggestions**](Suggestions.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_similar_images**
> ImageSearchResults get_similar_images(id, language=language, page=page, per_page=per_page, view=view)

List similar images

This endpoint returns images that are visually similar to an image that you specify.

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
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
id = 'id_example' # str | Image ID
language = shutterstock_sdk.Language() # Language | Language for the keywords and categories in the response (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
view = 'minimal' # str | Amount of detail to render in the response (optional) (default to minimal)

try:
    # List similar images
    api_response = api_instance.get_similar_images(id, language=language, page=page, per_page=per_page, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_similar_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Image ID | 
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

# **get_updated_images**
> UpdatedMediaDataList get_updated_images(type=type, start_date=start_date, end_date=end_date, interval=interval, page=page, per_page=per_page, sort=sort)

List updated images

This endpoint lists images that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the `interval` parameter to show images that were updated recently, but you can also use the `start_date` and `end_date` parameters to specify a range of no more than three days. Do not use the `interval` parameter with either `start_date` or `end_date`.

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
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
type = ['type_example'] # list[str] | Show images that were added, deleted, or edited; by default, the endpoint returns images that were updated in any of these ways (optional)
start_date = '2013-10-20' # date | Show images updated on or after the specified date (optional)
end_date = '2013-10-20' # date | Show images updated before the specified date (optional)
interval = '1 HOUR' # str | Show images updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows images that were updated in the hour preceding the request (optional) (default to 1 HOUR)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Number of results per page (optional) (default to 100)
sort = 'newest' # str | Sort order (optional) (default to newest)

try:
    # List updated images
    api_response = api_instance.get_updated_images(type=type, start_date=start_date, end_date=end_date, interval=interval, page=page, per_page=per_page, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_updated_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**list[str]**](str.md)| Show images that were added, deleted, or edited; by default, the endpoint returns images that were updated in any of these ways | [optional] 
 **start_date** | **date**| Show images updated on or after the specified date | [optional] 
 **end_date** | **date**| Show images updated before the specified date | [optional] 
 **interval** | **str**| Show images updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows images that were updated in the hour preceding the request | [optional] [default to 1 HOUR]
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 100]
 **sort** | **str**| Sort order | [optional] [default to newest]

### Return type

[**UpdatedMediaDataList**](UpdatedMediaDataList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_images**
> LicenseImageResultDataList license_images(body, subscription_id=subscription_id, format=format, size=size, search_id=search_id)

License images

This endpoint gets licenses for one or more images. You must specify the image IDs in the body parameter and other details like the format, size, and subscription ID either in the query parameter or with each image ID in the body parameter. Values in the body parameter override values in the query parameters.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
body = shutterstock_sdk.LicenseImageRequest() # LicenseImageRequest | List of images to request licenses for and information about each license transaction; these values override the defaults in the query parameters
subscription_id = 'subscription_id_example' # str | Subscription ID to use to license the image (optional)
format = 'jpg' # str | Image format (optional) (default to jpg)
size = 'huge' # str | Image size (optional) (default to huge)
search_id = 'search_id_example' # str | Search ID that was provided in the results of an image search (optional)

try:
    # License images
    api_response = api_instance.license_images(body, subscription_id=subscription_id, format=format, size=size, search_id=search_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->license_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LicenseImageRequest**](LicenseImageRequest.md)| List of images to request licenses for and information about each license transaction; these values override the defaults in the query parameters | 
 **subscription_id** | **str**| Subscription ID to use to license the image | [optional] 
 **format** | **str**| Image format | [optional] [default to jpg]
 **size** | **str**| Image size | [optional] [default to huge]
 **search_id** | **str**| Search ID that was provided in the results of an image search | [optional] 

### Return type

[**LicenseImageResultDataList**](LicenseImageResultDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_image_categories**
> CategoryDataList list_image_categories(language=language)

List image categories

This endpoint lists the categories (Shutterstock-assigned genres) that images can belong to.

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
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
language = shutterstock_sdk.Language() # Language | Language for the keywords and categories in the response (optional)

try:
    # List image categories
    api_response = api_instance.list_image_categories(language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->list_image_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] 

### Return type

[**CategoryDataList**](CategoryDataList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_image_collection**
> rename_image_collection(body, id)

Rename image collections

This endpoint sets a new name for an image collection.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
body = shutterstock_sdk.CollectionUpdateRequest() # CollectionUpdateRequest | The new name for the collection
id = 'id_example' # str | Collection ID

try:
    # Rename image collections
    api_instance.rename_image_collection(body, id)
except ApiException as e:
    print("Exception when calling ImagesApi->rename_image_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionUpdateRequest**](CollectionUpdateRequest.md)| The new name for the collection | 
 **id** | **str**| Collection ID | 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_images**
> ImageSearchResults search_images(added_date=added_date, added_date_start=added_date_start, aspect_ratio_min=aspect_ratio_min, aspect_ratio_max=aspect_ratio_max, aspect_ratio=aspect_ratio, added_date_end=added_date_end, category=category, color=color, contributor=contributor, contributor_country=contributor_country, fields=fields, height=height, height_from=height_from, height_to=height_to, image_type=image_type, keyword_safe_search=keyword_safe_search, language=language, license=license, model=model, orientation=orientation, page=page, per_page=per_page, people_model_released=people_model_released, people_age=people_age, people_ethnicity=people_ethnicity, people_gender=people_gender, people_number=people_number, query=query, region=region, safe=safe, sort=sort, spellcheck_query=spellcheck_query, view=view, width=width, width_from=width_from, width_to=width_to)

Search for images

This endpoint searches for images. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the `query` parameter by prefixing the term with NOT. Free API accounts show results only from a limited library of media, not the full Shutterstock media library. Also, the number of search fields they can use in a request is limited.

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
api_instance = shutterstock_sdk.ImagesApi(shutterstock_sdk.ApiClient(configuration))
added_date = '2013-10-20' # date | Show images added on the specified date (optional)
added_date_start = '2013-10-20' # date | Show images added on or after the specified date (optional)
aspect_ratio_min = 1.2 # float | Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image (optional)
aspect_ratio_max = 1.2 # float | Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image (optional)
aspect_ratio = 1.2 # float | Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image (optional)
added_date_end = '2013-10-20' # date | Show images added before the specified date (optional)
category = 'category_example' # str | Show images with the specified Shutterstock-defined category; specify a category name or ID (optional)
color = 'color_example' # str | Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that use similar colors (optional)
contributor = ['contributor_example'] # list[str] | Show images with the specified contributor names or IDs, allows multiple (optional)
contributor_country = shutterstock_sdk.ContributorCountry() # ContributorCountry | Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search (optional)
fields = 'fields_example' # str | Fields to display in the response; see the documentation for the fields parameter in the overview section (optional)
height = 56 # int | (Deprecated; use height_from and height_to instead) Show images with the specified height (optional)
height_from = 56 # int | Show images with the specified height or larger, in pixels (optional)
height_to = 56 # int | Show images with the specified height or smaller, in pixels (optional)
image_type = ['image_type_example'] # list[str] | Show images of the specified type (optional)
keyword_safe_search = true # bool | Hide results with potentially unsafe keywords (optional) (default to true)
language = shutterstock_sdk.Language() # Language | Set query and result language (uses Accept-Language header if not set) (optional)
license = ['license_example'] # list[str] | Show only images with the specified license (optional)
model = ['model_example'] # list[str] | Show image results with the specified model IDs (optional)
orientation = 'orientation_example' # str | Show image results with horizontal or vertical orientation (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
people_model_released = true # bool | Show images of people with a signed model release (optional)
people_age = 'people_age_example' # str | Show images that feature people of the specified age category (optional)
people_ethnicity = ['people_ethnicity_example'] # list[str] | Show images with people of the specified ethnicities (optional)
people_gender = 'people_gender_example' # str | Show images with people of the specified gender (optional)
people_number = 56 # int | Show images with the specified number of people (optional)
query = 'query_example' # str | One or more search terms separated by spaces; you can use NOT to filter out images that match a term (optional)
region = shutterstock_sdk.Region() # Region | Raise or lower search result rankings based on the result's relevance to a specified region; you can provide a country code or an IP address from which the API infers a country (optional)
safe = true # bool | Enable or disable safe search (optional) (default to true)
sort = 'popular' # str | Sort by (optional) (default to popular)
spellcheck_query = true # bool | Spellcheck the search query and return results on suggested spellings (optional) (default to true)
view = 'minimal' # str | Amount of detail to render in the response (optional) (default to minimal)
width = 56 # int | (Deprecated; use width_from and width_to instead) Show images with the specified width (optional)
width_from = 56 # int | Show images with the specified width or larger, in pixels (optional)
width_to = 56 # int | Show images with the specified width or smaller, in pixels (optional)

try:
    # Search for images
    api_response = api_instance.search_images(added_date=added_date, added_date_start=added_date_start, aspect_ratio_min=aspect_ratio_min, aspect_ratio_max=aspect_ratio_max, aspect_ratio=aspect_ratio, added_date_end=added_date_end, category=category, color=color, contributor=contributor, contributor_country=contributor_country, fields=fields, height=height, height_from=height_from, height_to=height_to, image_type=image_type, keyword_safe_search=keyword_safe_search, language=language, license=license, model=model, orientation=orientation, page=page, per_page=per_page, people_model_released=people_model_released, people_age=people_age, people_ethnicity=people_ethnicity, people_gender=people_gender, people_number=people_number, query=query, region=region, safe=safe, sort=sort, spellcheck_query=spellcheck_query, view=view, width=width, width_from=width_from, width_to=width_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->search_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **added_date** | **date**| Show images added on the specified date | [optional] 
 **added_date_start** | **date**| Show images added on or after the specified date | [optional] 
 **aspect_ratio_min** | **float**| Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] 
 **aspect_ratio_max** | **float**| Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] 
 **aspect_ratio** | **float**| Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] 
 **added_date_end** | **date**| Show images added before the specified date | [optional] 
 **category** | **str**| Show images with the specified Shutterstock-defined category; specify a category name or ID | [optional] 
 **color** | **str**| Specify either a hexadecimal color in the format &#x27;4F21EA&#x27; or &#x27;grayscale&#x27;; the API returns images that use similar colors | [optional] 
 **contributor** | [**list[str]**](str.md)| Show images with the specified contributor names or IDs, allows multiple | [optional] 
 **contributor_country** | [**ContributorCountry**](.md)| Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search | [optional] 
 **fields** | **str**| Fields to display in the response; see the documentation for the fields parameter in the overview section | [optional] 
 **height** | **int**| (Deprecated; use height_from and height_to instead) Show images with the specified height | [optional] 
 **height_from** | **int**| Show images with the specified height or larger, in pixels | [optional] 
 **height_to** | **int**| Show images with the specified height or smaller, in pixels | [optional] 
 **image_type** | [**list[str]**](str.md)| Show images of the specified type | [optional] 
 **keyword_safe_search** | **bool**| Hide results with potentially unsafe keywords | [optional] [default to true]
 **language** | [**Language**](.md)| Set query and result language (uses Accept-Language header if not set) | [optional] 
 **license** | [**list[str]**](str.md)| Show only images with the specified license | [optional] 
 **model** | [**list[str]**](str.md)| Show image results with the specified model IDs | [optional] 
 **orientation** | **str**| Show image results with horizontal or vertical orientation | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **people_model_released** | **bool**| Show images of people with a signed model release | [optional] 
 **people_age** | **str**| Show images that feature people of the specified age category | [optional] 
 **people_ethnicity** | [**list[str]**](str.md)| Show images with people of the specified ethnicities | [optional] 
 **people_gender** | **str**| Show images with people of the specified gender | [optional] 
 **people_number** | **int**| Show images with the specified number of people | [optional] 
 **query** | **str**| One or more search terms separated by spaces; you can use NOT to filter out images that match a term | [optional] 
 **region** | [**Region**](.md)| Raise or lower search result rankings based on the result&#x27;s relevance to a specified region; you can provide a country code or an IP address from which the API infers a country | [optional] 
 **safe** | **bool**| Enable or disable safe search | [optional] [default to true]
 **sort** | **str**| Sort by | [optional] [default to popular]
 **spellcheck_query** | **bool**| Spellcheck the search query and return results on suggested spellings | [optional] [default to true]
 **view** | **str**| Amount of detail to render in the response | [optional] [default to minimal]
 **width** | **int**| (Deprecated; use width_from and width_to instead) Show images with the specified width | [optional] 
 **width_from** | **int**| Show images with the specified width or larger, in pixels | [optional] 
 **width_to** | **int**| Show images with the specified width or smaller, in pixels | [optional] 

### Return type

[**ImageSearchResults**](ImageSearchResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

