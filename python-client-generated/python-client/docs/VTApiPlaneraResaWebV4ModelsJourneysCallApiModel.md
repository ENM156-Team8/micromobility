# VTApiPlaneraResaWebV4ModelsJourneysCallApiModel

Information about a call on the trip leg.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stop_point** | [**VTApiPlaneraResaWebV4ModelsJourneysStopPointApiModel**](VTApiPlaneraResaWebV4ModelsJourneysStopPointApiModel.md) |  | 
**planned_time** | **str** | The planned time of the call in RFC 3339 format. | 
**estimated_time** | **str** | The estimated time of the call in RFC 3339 format. | [optional] 
**estimated_otherwise_planned_time** | **str** | The best known time of the call in RFC 3339 format. Is EstimatedTime if exists, otherwise PlannedTime. | [optional] [readonly] 
**notes** | [**List[VTApiPlaneraResaCoreModelsNote]**](VTApiPlaneraResaCoreModelsNote.md) | An ordered list (most important first) of notes related to the call. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journeys_call_api_model import VTApiPlaneraResaWebV4ModelsJourneysCallApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneysCallApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journeys_call_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneysCallApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneysCallApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journeys_call_api_model_dict = vt_api_planera_resa_web_v4_models_journeys_call_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneysCallApiModel from a dict
vt_api_planera_resa_web_v4_models_journeys_call_api_model_form_dict = vt_api_planera_resa_web_v4_models_journeys_call_api_model.from_dict(vt_api_planera_resa_web_v4_models_journeys_call_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


