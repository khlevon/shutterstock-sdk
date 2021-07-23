# AudioRenderResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The alphanumeric ID of the simple render | 
**timeline** | [**AudioRenderTimeline**](AudioRenderTimeline.md) |  | 
**status** | **str** | A coarse progress indicator | 
**preset** | **str** | The file format preset | [optional] 
**progress_percent** | **int** | The current progress of the render as a percentage | [optional] 
**files** | [**list[AudioRendersFilesList]**](AudioRendersFilesList.md) | The files associated with the render | [optional] 
**created_date** | **datetime** | The time the render was submitted to the API | [optional] 
**updated_date** | **datetime** | The time that the audio output was uploaded | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

