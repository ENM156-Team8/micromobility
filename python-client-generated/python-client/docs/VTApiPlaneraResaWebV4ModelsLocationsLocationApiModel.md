# VTApiPlaneraResaWebV4ModelsLocationsLocationApiModel

Information about a location.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | The 16-digit Västtrafik gid. | [optional] 
**name** | **str** | The location name. | 
**location_type** | [**VTApiPlaneraResaCoreModelsLocationType**](VTApiPlaneraResaCoreModelsLocationType.md) |  | 
**latitude** | **float** | The WGS84 latitude of the location. | [optional] 
**longitude** | **float** | The WGS84 longitude of the location. | [optional] 
**platform** | **str** | The location platform, only available for stop points. | [optional] 
**straight_line_distance_in_meters** | **int** | The location straight line distance in meters. | [optional] 
**has_local_service** | **bool** | Is \&quot;Närtrafik\&quot; (Local Service) available for the location?  Values are only available for LocationType: StopArea, PointOfInterest and Address.  Values are only available for endpoint: locations/by-text. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_locations_location_api_model import VTApiPlaneraResaWebV4ModelsLocationsLocationApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsLocationsLocationApiModel from a JSON string
vt_api_planera_resa_web_v4_models_locations_location_api_model_instance = VTApiPlaneraResaWebV4ModelsLocationsLocationApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsLocationsLocationApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_locations_location_api_model_dict = vt_api_planera_resa_web_v4_models_locations_location_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsLocationsLocationApiModel from a dict
vt_api_planera_resa_web_v4_models_locations_location_api_model_form_dict = vt_api_planera_resa_web_v4_models_locations_location_api_model.from_dict(vt_api_planera_resa_web_v4_models_locations_location_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


