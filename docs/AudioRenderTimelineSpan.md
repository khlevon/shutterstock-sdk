# AudioRenderTimelineSpan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | An identifier which must be unique within the parent span | [optional] 
**span_type** | **str** | Type of span; metered spans represent a pariod of time with music, and unmetered spans denote the end of the prior metered span | 
**time** | **int** | The absolute time, in seconds, at which the span starts | 
**tempo** | **int** | The tempo, in beats per minute, at the start of the span; if not provided, the API selects a random tempo | [optional] 
**regions** | [**list[AudioRenderTimelineSpanRegion]**](AudioRenderTimelineSpanRegion.md) | An array of region objects within the span | [optional] 
**instrument_groups** | [**list[AudioRenderTimelineSpanInstrumentGroup]**](AudioRenderTimelineSpanInstrumentGroup.md) | An array of instrument_group objects that are used in this span | [optional] 
**tempo_changes** | [**list[AudioRenderTimelineSpanTempoChanges]**](AudioRenderTimelineSpanTempoChanges.md) | Two or more inflection points in a tempo curve; the API creates a smoothly changing tempo by using a linear interpolation of the time between each tempo change | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

