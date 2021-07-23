# AudioRendersFilesList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The user-specified file name suggestion from the render request; this file name becomes the filename property of the Content-Disposition header when the user downloads the rendered audio file | 
**bits_sample** | **float** | The bit depth of the audio files in bits/sample | 
**content_type** | **str** | The content-type of the file | 
**download_url** | **str** | The internet-accessible URL from which the file can be downloaded. Any redirects encountered when using this URL must be followed | 
**frequency_hz** | **float** | The Sample rate of the audio files in Hertz (Hz) | 
**kbits_second** | **float** | The data rate of the audio files in kilobits/second | 
**size_bytes** | **float** | Size of the file in bytes | 
**tracks** | **list[str]** | An array of track names included in the file | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

