# VTApiPlaneraResaWebV4ModelsJourneysStopPointApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | The 16-digit Västtrafik gid of the stop point. | 
**name** | **str** | The stop point name. | 
**platform** | **str** | The platform of the stop point. | [optional] 
**latitude** | **float** | The latitude coordinate of the stop point. | [optional] 
**longitude** | **float** | The logitude coordinate of the stop point. | [optional] 
**stop_area** | [**VTApiPlaneraResaWebV4ModelsJourneysStopAreaApiModel**](VTApiPlaneraResaWebV4ModelsJourneysStopAreaApiModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journeys_stop_point_api_model import VTApiPlaneraResaWebV4ModelsJourneysStopPointApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneysStopPointApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journeys_stop_point_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneysStopPointApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneysStopPointApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journeys_stop_point_api_model_dict = vt_api_planera_resa_web_v4_models_journeys_stop_point_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneysStopPointApiModel from a dict
vt_api_planera_resa_web_v4_models_journeys_stop_point_api_model_form_dict = vt_api_planera_resa_web_v4_models_journeys_stop_point_api_model.from_dict(vt_api_planera_resa_web_v4_models_journeys_stop_point_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


