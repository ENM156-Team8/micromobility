# VTApiPlaneraResaWebV4ModelsApiError

Information about the error.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** | Error code. | [optional] 
**error_message** | **str** | More detailed description of the error. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_api_error import VTApiPlaneraResaWebV4ModelsApiError

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsApiError from a JSON string
vt_api_planera_resa_web_v4_models_api_error_instance = VTApiPlaneraResaWebV4ModelsApiError.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsApiError.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_api_error_dict = vt_api_planera_resa_web_v4_models_api_error_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsApiError from a dict
vt_api_planera_resa_web_v4_models_api_error_form_dict = vt_api_planera_resa_web_v4_models_api_error.from_dict(vt_api_planera_resa_web_v4_models_api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


