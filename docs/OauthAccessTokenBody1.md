# OauthAccessTokenBody1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Client ID (Consumer Key) of your application | 
**client_secret** | **str** | Client Secret (Consumer Secret) of your application | [optional] 
**code** | **str** | Response code from the /oauth/authorize flow; required if grant_type&#x3D;authorization_code | [optional] 
**grant_type** | **str** | Grant type: authorization_code generates user tokens, client_credentials generates short-lived client grants | 
**realm** | **str** | User type to be authorized (usually &#x27;customer&#x27;) | [optional] [default to 'customer']
**expires** | **bool** | Whether or not the token expires, expiring tokens come with a refresh_token to renew the access_token | [optional] [default to False]
**refresh_token** | **str** | Pass this along with grant_type&#x3D;refresh_token to get a fresh access token | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

