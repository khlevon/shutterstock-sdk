# shutterstock_sdk.UsersApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_token**](UsersApi.md#get_access_token) | **GET** /v2/user/access_token | Get access token details
[**get_user**](UsersApi.md#get_user) | **GET** /v2/user | Get user details
[**get_user_subscription_list**](UsersApi.md#get_user_subscription_list) | **GET** /v2/user/subscriptions | List user subscriptions

# **get_access_token**
> AccessTokenDetails get_access_token()

Get access token details

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
api_instance = shutterstock_sdk.UsersApi(shutterstock_sdk.ApiClient(configuration))

try:
    # Get access token details
    api_response = api_instance.get_access_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_access_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessTokenDetails**](AccessTokenDetails.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserDetails get_user()

Get user details

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
api_instance = shutterstock_sdk.UsersApi(shutterstock_sdk.ApiClient(configuration))

try:
    # Get user details
    api_response = api_instance.get_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDetails**](UserDetails.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subscription_list**
> SubscriptionDataList get_user_subscription_list()

List user subscriptions

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
api_instance = shutterstock_sdk.UsersApi(shutterstock_sdk.ApiClient(configuration))

try:
    # List user subscriptions
    api_response = api_instance.get_user_subscription_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_subscription_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SubscriptionDataList**](SubscriptionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

