# VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel

Information specifying the interval when valid journey information is available, i.e. when it is possible to search journeys.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_from** | **str** | The start time of the interval when valid journey information is available, specified in RFC 3339 format. | [optional] 
**valid_until** | **str** | The end time of the interval when valid journey information is available, specified in RFC 3339 format. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_valid_time_interval_api_model import VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel from a JSON string
vt_api_planera_resa_web_v4_models_valid_time_interval_api_model_instance = VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_valid_time_interval_api_model_dict = vt_api_planera_resa_web_v4_models_valid_time_interval_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel from a dict
vt_api_planera_resa_web_v4_models_valid_time_interval_api_model_form_dict = vt_api_planera_resa_web_v4_models_valid_time_interval_api_model.from_dict(vt_api_planera_resa_web_v4_models_valid_time_interval_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


