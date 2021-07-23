# shutterstock_sdk.OauthApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize**](OauthApi.md#authorize) | **GET** /v2/oauth/authorize | Authorize applications
[**create_access_token**](OauthApi.md#create_access_token) | **POST** /v2/oauth/access_token | Get access tokens

# **authorize**
> authorize(client_id, redirect_uri, response_type, state, realm=realm, scope=scope)

Authorize applications

This endpoint returns a redirect URI (in the 'Location' header) that the customer uses to authorize your application and, together with POST /v2/oauth/access_token, generate an access token that represents that authorization.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = shutterstock_sdk.OauthApi()
client_id = 'client_id_example' # str | Client ID (Consumer Key) of your application
redirect_uri = 'redirect_uri_example' # str | The callback URI to send the request to after authorization; must use a host name that is registered with your application
response_type = 'response_type_example' # str | Type of temporary authorization code that will be used to generate an access code; the only valid value is 'code'
state = 'state_example' # str | Unique value used by the calling app to verify the request
realm = 'customer' # str | User type to be authorized (usually 'customer') (optional) (default to customer)
scope = 'user.view' # str | Space-separated list of scopes to be authorized (optional) (default to user.view)

try:
    # Authorize applications
    api_instance.authorize(client_id, redirect_uri, response_type, state, realm=realm, scope=scope)
except ApiException as e:
    print("Exception when calling OauthApi->authorize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Client ID (Consumer Key) of your application | 
 **redirect_uri** | **str**| The callback URI to send the request to after authorization; must use a host name that is registered with your application | 
 **response_type** | **str**| Type of temporary authorization code that will be used to generate an access code; the only valid value is &#x27;code&#x27; | 
 **state** | **str**| Unique value used by the calling app to verify the request | 
 **realm** | **str**| User type to be authorized (usually &#x27;customer&#x27;) | [optional] [default to customer]
 **scope** | **str**| Space-separated list of scopes to be authorized | [optional] [default to user.view]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_access_token**
> OauthAccessTokenResponse create_access_token(client_id=client_id, client_secret=client_secret, code=code, grant_type=grant_type, realm=realm, expires=expires, refresh_token=refresh_token)

Get access tokens

This endpoint returns an access token for the specified user and with the specified scopes. The token does not expire until the user changes their password. The body parameters must be encoded as form data.

### Example
```python
from __future__ import print_function
import time
import shutterstock_sdk
from shutterstock_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = shutterstock_sdk.OauthApi()
client_id = 'client_id_example' # str |  (optional)
client_secret = 'client_secret_example' # str |  (optional)
code = 'code_example' # str |  (optional)
grant_type = 'grant_type_example' # str |  (optional)
realm = 'realm_example' # str |  (optional)
expires = 'expires_example' # str |  (optional)
refresh_token = 'refresh_token_example' # str |  (optional)

try:
    # Get access tokens
    api_response = api_instance.create_access_token(client_id=client_id, client_secret=client_secret, code=code, grant_type=grant_type, realm=realm, expires=expires, refresh_token=refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthApi->create_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 
 **code** | **str**|  | [optional] 
 **grant_type** | **str**|  | [optional] 
 **realm** | **str**|  | [optional] 
 **expires** | **str**|  | [optional] 
 **refresh_token** | **str**|  | [optional] 

### Return type

[**OauthAccessTokenResponse**](OauthAccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

