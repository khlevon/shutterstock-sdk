# Descriptors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the descriptor | [optional] 
**average_render_speed** | **float** | The average ratio of the length of the music to the time it takes to render; for example, a render speed of 3.0 generates 30 seconds of music in about 10 seconds | [optional] 
**bands** | [**list[Bands]**](Bands.md) | The bands that are available to use this descriptor | [optional] 
**instruments** | [**list[Instruments]**](Instruments.md) | The instruments that can play with this descriptor | [optional] 
**max_tempo** | **float** | The maximum beats per minute that the descriptor is intended to be used with | [optional] 
**min_tempo** | **float** | The minimum beats per minute that the descriptor is intended to be used with | [optional] 
**name** | **str** | The name of the descriptor | [optional] 
**previews** | [**list[Preview]**](Preview.md) | Preview of the descriptor | [optional] 
**tags** | **list[str]** | Tags that describe the descriptor | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

