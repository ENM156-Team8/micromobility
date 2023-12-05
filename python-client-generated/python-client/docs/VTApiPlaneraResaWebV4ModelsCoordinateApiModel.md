# VTApiPlaneraResaWebV4ModelsCoordinateApiModel

Information about the coordinates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | The latitude of this position (WGS84). | [optional] 
**longitude** | **float** | The longitude of this position (WGS84). | [optional] 
**elevation** | **float** | The elevation of this position (WGS84). | [optional] 
**is_on_trip_leg** | **bool** | The coordinate is on the tripleg. | [optional] 
**is_trip_leg_start** | **bool** | The coordinate is on the first call of the leg. | [optional] 
**is_trip_leg_stop** | **bool** | The coordinate is on the last call of the leg. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_coordinate_api_model import VTApiPlaneraResaWebV4ModelsCoordinateApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsCoordinateApiModel from a JSON string
vt_api_planera_resa_web_v4_models_coordinate_api_model_instance = VTApiPlaneraResaWebV4ModelsCoordinateApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsCoordinateApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_coordinate_api_model_dict = vt_api_planera_resa_web_v4_models_coordinate_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsCoordinateApiModel from a dict
vt_api_planera_resa_web_v4_models_coordinate_api_model_form_dict = vt_api_planera_resa_web_v4_models_coordinate_api_model.from_dict(vt_api_planera_resa_web_v4_models_coordinate_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


