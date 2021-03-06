# Subscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allotment** | [**Allotment**](Allotment.md) |  | [optional] 
**description** | **str** | Description of the subscription | [optional] 
**expiration_time** | **datetime** | Date the subscription ends | [optional] 
**formats** | [**list[LicenseFormat]**](LicenseFormat.md) | List of formats that are licensable for the subscription | [optional] 
**id** | **str** | Unique internal identifier for the subscription | 
**license** | **str** | Internal identifier for the type of subscription | [optional] 
**asset_type** | **str** | Identifier for the type of assets associated with this subscription (images, videos, audio, editorial) | [optional] 
**metadata** | [**SubscriptionMetadata**](SubscriptionMetadata.md) |  | [optional] 
**price_per_download** | [**Price**](Price.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

