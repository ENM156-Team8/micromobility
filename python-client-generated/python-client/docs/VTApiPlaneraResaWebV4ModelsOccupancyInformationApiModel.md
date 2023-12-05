# VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel

Contains information about occupancy.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | [**VTApiPlaneraResaWebV4ModelsOccupancyLevel**](VTApiPlaneraResaWebV4ModelsOccupancyLevel.md) |  | [optional] 
**source** | [**VTApiPlaneraResaWebV4ModelsOccupancyInformationSource**](VTApiPlaneraResaWebV4ModelsOccupancyInformationSource.md) |  | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_occupancy_information_api_model import VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel from a JSON string
vt_api_planera_resa_web_v4_models_occupancy_information_api_model_instance = VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_occupancy_information_api_model_dict = vt_api_planera_resa_web_v4_models_occupancy_information_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel from a dict
vt_api_planera_resa_web_v4_models_occupancy_information_api_model_form_dict = vt_api_planera_resa_web_v4_models_occupancy_information_api_model.from_dict(vt_api_planera_resa_web_v4_models_occupancy_information_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


