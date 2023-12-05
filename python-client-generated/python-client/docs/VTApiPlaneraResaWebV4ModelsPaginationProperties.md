# VTApiPlaneraResaWebV4ModelsPaginationProperties

Pagination information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The requested number of results. | [optional] 
**offset** | **int** | The requested offset in the results array. | [optional] 
**size** | **int** | The actual number of returned results. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_pagination_properties import VTApiPlaneraResaWebV4ModelsPaginationProperties

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsPaginationProperties from a JSON string
vt_api_planera_resa_web_v4_models_pagination_properties_instance = VTApiPlaneraResaWebV4ModelsPaginationProperties.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsPaginationProperties.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_pagination_properties_dict = vt_api_planera_resa_web_v4_models_pagination_properties_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsPaginationProperties from a dict
vt_api_planera_resa_web_v4_models_pagination_properties_form_dict = vt_api_planera_resa_web_v4_models_pagination_properties.from_dict(vt_api_planera_resa_web_v4_models_pagination_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


