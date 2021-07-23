# OauthAccessTokenResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Access token that can be used for future requests | 
**expires_in** | **int** | Number of seconds before token expires, only present for expiring tokens | [optional] 
**token_type** | **str** | Type of token | [default to 'Bearer']
**refresh_token** | **str** | A refresh token that can be used to renew the access_token when it expires, only present for expiring tokens | [optional] 
**user_token** | **str** | Metadata about the access_token, only present for expiring tokens | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

