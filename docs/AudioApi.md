# shutterstock_sdk.AudioApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_track_collection_items**](AudioApi.md#add_track_collection_items) | **POST** /v2/audio/collections/{id}/items | Add audio tracks to collections
[**create_track_collection**](AudioApi.md#create_track_collection) | **POST** /v2/audio/collections | Create audio collections
[**delete_track_collection**](AudioApi.md#delete_track_collection) | **DELETE** /v2/audio/collections/{id} | Delete audio collections
[**delete_track_collection_items**](AudioApi.md#delete_track_collection_items) | **DELETE** /v2/audio/collections/{id}/items | Remove audio tracks from collections
[**download_tracks**](AudioApi.md#download_tracks) | **POST** /v2/audio/licenses/{id}/downloads | Download audio tracks
[**get_track**](AudioApi.md#get_track) | **GET** /v2/audio/{id} | Get details about audio tracks
[**get_track_collection**](AudioApi.md#get_track_collection) | **GET** /v2/audio/collections/{id} | Get the details of audio collections
[**get_track_collection_items**](AudioApi.md#get_track_collection_items) | **GET** /v2/audio/collections/{id}/items | Get the contents of audio collections
[**get_track_collection_list**](AudioApi.md#get_track_collection_list) | **GET** /v2/audio/collections | List audio collections
[**get_track_license_list**](AudioApi.md#get_track_license_list) | **GET** /v2/audio/licenses | List audio licenses
[**get_track_list**](AudioApi.md#get_track_list) | **GET** /v2/audio | List audio tracks
[**license_track**](AudioApi.md#license_track) | **POST** /v2/audio/licenses | License audio tracks
[**list_genres**](AudioApi.md#list_genres) | **GET** /v2/audio/genres | List audio genres
[**list_instruments**](AudioApi.md#list_instruments) | **GET** /v2/audio/instruments | List audio instruments
[**list_moods**](AudioApi.md#list_moods) | **GET** /v2/audio/moods | List audio moods
[**rename_track_collection**](AudioApi.md#rename_track_collection) | **POST** /v2/audio/collections/{id} | Rename audio collections
[**search_tracks**](AudioApi.md#search_tracks) | **GET** /v2/audio/search | Search for tracks

# **add_track_collection_items**
> add_track_collection_items(body, id)

Add audio tracks to collections

This endpoint adds one or more tracks to a collection by track IDs.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))
body = shutterstock_sdk.CollectionItemRequest() # CollectionItemRequest | List of items to add to collection
id = 'id_example' # str | Collection ID

try:
    # Add audio tracks to collections
    api_instance.add_track_collection_items(body, id)
except ApiException as e:
    print("Exception when calling AudioApi->add_track_collection_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionItemRequest**](CollectionItemRequest.md)| List of items to add to collection | 
 **id** | **str**| Collection ID | 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_track_collection**
> CollectionCreateResponse create_track_collection(body)

Create audio collections

This endpoint creates one or more collections (soundboxes). To add tracks, use `POST /v2/audio/collections/{id}/items`.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))
body = shutterstock_sdk.CollectionCreateRequest() # CollectionCreateRequest | Collection metadata

try:
    # Create audio collections
    api_response = api_instance.create_track_collection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->create_track_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionCreateRequest**](CollectionCreateRequest.md)| Collection metadata | 

### Return type

[**CollectionCreateResponse**](CollectionCreateResponse.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_track_collection**
> delete_track_collection(id)

Delete audio collections

This endpoint deletes a collection.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))
id = 'id_example' # str | Collection ID

try:
    # Delete audio collections
    api_instance.delete_track_collection(id)
except ApiException as e:
    print("Exception when calling AudioApi->delete_track_collection: %s\n" % e)
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

# **delete_track_collection_items**
> delete_track_collection_items(id, item_id=item_id)

Remove audio tracks from collections

This endpoint removes one or more tracks from a collection.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))
id = 'id_example' # str | Collection ID
item_id = ['item_id_example'] # list[str] | One or more item IDs to remove from the collection (optional)

try:
    # Remove audio tracks from collections
    api_instance.delete_track_collection_items(id, item_id=item_id)
except ApiException as e:
    print("Exception when calling AudioApi->delete_track_collection_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **item_id** | [**list[str]**](str.md)| One or more item IDs to remove from the collection | [optional] 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_tracks**
> Url download_tracks(id)

Download audio tracks

This endpoint redownloads tracks that you have already received a license for.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))
id = 'id_example' # str | License ID

try:
    # Download audio tracks
    api_response = api_instance.download_tracks(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->download_tracks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| License ID | 

### Return type

[**Url**](Url.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_track**
> Audio get_track(id, view=view)

Get details about audio tracks

This endpoint shows information about a track, including its genres, instruments, and other attributes.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))
id = 56 # int | Audio track ID
view = 'full' # str | Amount of detail to render in the response (optional) (default to full)

try:
    # Get details about audio tracks
    api_response = api_instance.get_track(id, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->get_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Audio track ID | 
 **view** | **str**| Amount of detail to render in the response | [optional] [default to full]

### Return type

[**Audio**](Audio.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_track_collection**
> Collection get_track_collection(id)

Get the details of audio collections

This endpoint gets more detailed information about a collection, including the number of items in it and when it was last updated. To get the tracks in collections, use `GET /v2/audio/collections/{id}/items`.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))
id = 'id_example' # str | Collection ID

try:
    # Get the details of audio collections
    api_response = api_instance.get_track_collection(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->get_track_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 

### Return type

[**Collection**](Collection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_track_collection_items**
> CollectionItemDataList get_track_collection_items(id, page=page, per_page=per_page, sort=sort)

Get the contents of audio collections

This endpoint lists the IDs of tracks in a collection and the date that each was added.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))
id = 'id_example' # str | Collection ID
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Number of results per page (optional) (default to 100)
sort = 'oldest' # str | Sort order (optional) (default to oldest)

try:
    # Get the contents of audio collections
    api_response = api_instance.get_track_collection_items(id, page=page, per_page=per_page, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->get_track_collection_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 100]
 **sort** | **str**| Sort order | [optional] [default to oldest]

### Return type

[**CollectionItemDataList**](CollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_track_collection_list**
> CollectionDataList get_track_collection_list(page=page, per_page=per_page)

List audio collections

This endpoint lists your collections of audio tracks and their basic attributes.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Number of results per page (optional) (default to 100)

try:
    # List audio collections
    api_response = api_instance.get_track_collection_list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->get_track_collection_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_track_license_list**
> DownloadHistoryDataList get_track_license_list(audio_id=audio_id, license=license, page=page, per_page=per_page, sort=sort, username=username, start_date=start_date, end_date=end_date)

List audio licenses

This endpoint lists existing licenses. You can filter the results according to the track ID to see if you have an existing license for a specific track.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))
audio_id = 'audio_id_example' # str | Show licenses for the specified track ID (optional)
license = 'license_example' # str | Restrict results by license. Prepending a `-` sign will exclude results by license (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
sort = 'newest' # str | Sort order (optional) (default to newest)
username = 'username_example' # str | Filter licenses by username of licensee (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Show licenses created on or after the specified date (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Show licenses created before the specified date (optional)

try:
    # List audio licenses
    api_response = api_instance.get_track_license_list(audio_id=audio_id, license=license, page=page, per_page=per_page, sort=sort, username=username, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->get_track_license_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audio_id** | **str**| Show licenses for the specified track ID | [optional] 
 **license** | **str**| Restrict results by license. Prepending a &#x60;-&#x60; sign will exclude results by license | [optional] 
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

# **get_track_list**
> AudioDataList get_track_list(id, view=view)

List audio tracks

This endpoint lists information about one or more audio tracks, including the description and publication date.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))
id = ['id_example'] # list[str] | One or more audio IDs
view = 'minimal' # str | Amount of detail to render in the response (optional) (default to minimal)

try:
    # List audio tracks
    api_response = api_instance.get_track_list(id, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->get_track_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| One or more audio IDs | 
 **view** | **str**| Amount of detail to render in the response | [optional] [default to minimal]

### Return type

[**AudioDataList**](AudioDataList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_track**
> LicenseAudioResultDataList license_track(body, license=license, search_id=search_id)

License audio tracks

This endpoint gets licenses for one or more tracks.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))
body = shutterstock_sdk.LicenseAudioRequest() # LicenseAudioRequest | Tracks to license
license = 'license_example' # str | License type (optional)
search_id = 'search_id_example' # str | The ID of the search that led to licensing this track (optional)

try:
    # License audio tracks
    api_response = api_instance.license_track(body, license=license, search_id=search_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->license_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LicenseAudioRequest**](LicenseAudioRequest.md)| Tracks to license | 
 **license** | **str**| License type | [optional] 
 **search_id** | **str**| The ID of the search that led to licensing this track | [optional] 

### Return type

[**LicenseAudioResultDataList**](LicenseAudioResultDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_genres**
> GenreList list_genres()

List audio genres

This endpoint returns a list of all audio genres.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))

try:
    # List audio genres
    api_response = api_instance.list_genres()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->list_genres: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GenreList**](GenreList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_instruments**
> InstrumentList list_instruments()

List audio instruments

This endpoint returns a list of all audio instruments.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))

try:
    # List audio instruments
    api_response = api_instance.list_instruments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->list_instruments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InstrumentList**](InstrumentList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_moods**
> MoodList list_moods()

List audio moods

This endpoint returns a list of all audio moods.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))

try:
    # List audio moods
    api_response = api_instance.list_moods()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->list_moods: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MoodList**](MoodList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_track_collection**
> rename_track_collection(body, id)

Rename audio collections

This endpoint sets a new name for a collection.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))
body = shutterstock_sdk.CollectionUpdateRequest() # CollectionUpdateRequest | Collection changes
id = 'id_example' # str | Collection ID

try:
    # Rename audio collections
    api_instance.rename_track_collection(body, id)
except ApiException as e:
    print("Exception when calling AudioApi->rename_track_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionUpdateRequest**](CollectionUpdateRequest.md)| Collection changes | 
 **id** | **str**| Collection ID | 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tracks**
> AudioSearchResults search_tracks(artists=artists, bpm=bpm, bpm_from=bpm_from, bpm_to=bpm_to, duration=duration, duration_from=duration_from, duration_to=duration_to, genre=genre, is_instrumental=is_instrumental, instruments=instruments, moods=moods, page=page, per_page=per_page, query=query, sort=sort, sort_order=sort_order, vocal_description=vocal_description, view=view, fields=fields, library=library, language=language)

Search for tracks

This endpoint searches for tracks. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter.

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
api_instance = shutterstock_sdk.AudioApi(shutterstock_sdk.ApiClient(configuration))
artists = ['artists_example'] # list[str] | Show tracks with one of the specified artist names or IDs (optional)
bpm = 56 # int | (Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute (optional)
bpm_from = 56 # int | Show tracks with the specified beats per minute or faster (optional)
bpm_to = 56 # int | Show tracks with the specified beats per minute or slower (optional)
duration = 56 # int | Show tracks with the specified duration in seconds (optional)
duration_from = 56 # int | Show tracks with the specified duration or longer in seconds (optional)
duration_to = 56 # int | Show tracks with the specified duration or shorter in seconds (optional)
genre = ['genre_example'] # list[str] | Show tracks with each of the specified genres; to get the list of genres, use `GET /v2/audio/genres` (optional)
is_instrumental = true # bool | Show instrumental music only (optional)
instruments = ['instruments_example'] # list[str] | Show tracks with each of the specified instruments; to get the list of instruments, use `GET /v2/audio/instruments` (optional)
moods = ['moods_example'] # list[str] | Show tracks with each of the specified moods; to get the list of moods, use `GET /v2/audio/moods` (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
query = 'query_example' # str | One or more search terms separated by spaces (optional)
sort = 'sort_example' # str | Sort by (optional)
sort_order = 'desc' # str | Sort order (optional) (default to desc)
vocal_description = 'vocal_description_example' # str | Show tracks with the specified vocal description (male, female) (optional)
view = 'minimal' # str | Amount of detail to render in the response (optional) (default to minimal)
fields = 'fields_example' # str | Fields to display in the response; see the documentation for the fields parameter in the overview section (optional)
library = 'premier' # str | Which library to search (optional) (default to premier)
language = 'language_example' # str | Which language to search in (optional)

try:
    # Search for tracks
    api_response = api_instance.search_tracks(artists=artists, bpm=bpm, bpm_from=bpm_from, bpm_to=bpm_to, duration=duration, duration_from=duration_from, duration_to=duration_to, genre=genre, is_instrumental=is_instrumental, instruments=instruments, moods=moods, page=page, per_page=per_page, query=query, sort=sort, sort_order=sort_order, vocal_description=vocal_description, view=view, fields=fields, library=library, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->search_tracks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artists** | [**list[str]**](str.md)| Show tracks with one of the specified artist names or IDs | [optional] 
 **bpm** | **int**| (Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute | [optional] 
 **bpm_from** | **int**| Show tracks with the specified beats per minute or faster | [optional] 
 **bpm_to** | **int**| Show tracks with the specified beats per minute or slower | [optional] 
 **duration** | **int**| Show tracks with the specified duration in seconds | [optional] 
 **duration_from** | **int**| Show tracks with the specified duration or longer in seconds | [optional] 
 **duration_to** | **int**| Show tracks with the specified duration or shorter in seconds | [optional] 
 **genre** | [**list[str]**](str.md)| Show tracks with each of the specified genres; to get the list of genres, use &#x60;GET /v2/audio/genres&#x60; | [optional] 
 **is_instrumental** | **bool**| Show instrumental music only | [optional] 
 **instruments** | [**list[str]**](str.md)| Show tracks with each of the specified instruments; to get the list of instruments, use &#x60;GET /v2/audio/instruments&#x60; | [optional] 
 **moods** | [**list[str]**](str.md)| Show tracks with each of the specified moods; to get the list of moods, use &#x60;GET /v2/audio/moods&#x60; | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **query** | **str**| One or more search terms separated by spaces | [optional] 
 **sort** | **str**| Sort by | [optional] 
 **sort_order** | **str**| Sort order | [optional] [default to desc]
 **vocal_description** | **str**| Show tracks with the specified vocal description (male, female) | [optional] 
 **view** | **str**| Amount of detail to render in the response | [optional] [default to minimal]
 **fields** | **str**| Fields to display in the response; see the documentation for the fields parameter in the overview section | [optional] 
 **library** | **str**| Which library to search | [optional] [default to premier]
 **language** | **str**| Which language to search in | [optional] 

### Return type

[**AudioSearchResults**](AudioSearchResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

