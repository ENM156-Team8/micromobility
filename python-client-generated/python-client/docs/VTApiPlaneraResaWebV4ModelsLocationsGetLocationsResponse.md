# VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse

The response to a get locations request, includes the results and pagination information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[VTApiPlaneraResaWebV4ModelsLocationsLocationApiModel]**](VTApiPlaneraResaWebV4ModelsLocationsLocationApiModel.md) | The results. | [optional] 
**pagination** | [**VTApiPlaneraResaWebV4ModelsPaginationProperties**](VTApiPlaneraResaWebV4ModelsPaginationProperties.md) |  | [optional] 
**links** | [**VTApiPlaneraResaWebV4ModelsPaginationLinks**](VTApiPlaneraResaWebV4ModelsPaginationLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_locations_get_locations_response import VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse from a JSON string
vt_api_planera_resa_web_v4_models_locations_get_locations_response_instance = VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_locations_get_locations_response_dict = vt_api_planera_resa_web_v4_models_locations_get_locations_response_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse from a dict
vt_api_planera_resa_web_v4_models_locations_get_locations_response_form_dict = vt_api_planera_resa_web_v4_models_locations_get_locations_response.from_dict(vt_api_planera_resa_web_v4_models_locations_get_locations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


