# VTApiPlaneraResaWebV4ModelsPaginationLinks

Pagination navigation links.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | **str** | Link to the previous results page, if available, otherwise null. | [optional] 
**next** | **str** | Link to the next results page, if available, otherwise null. Not guaranteed to give a result if called. | [optional] 
**current** | **str** | Link to the current results page, if available, otherwise null. Not guaranteed to give a result if called. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_pagination_links import VTApiPlaneraResaWebV4ModelsPaginationLinks

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsPaginationLinks from a JSON string
vt_api_planera_resa_web_v4_models_pagination_links_instance = VTApiPlaneraResaWebV4ModelsPaginationLinks.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsPaginationLinks.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_pagination_links_dict = vt_api_planera_resa_web_v4_models_pagination_links_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsPaginationLinks from a dict
vt_api_planera_resa_web_v4_models_pagination_links_form_dict = vt_api_planera_resa_web_v4_models_pagination_links.from_dict(vt_api_planera_resa_web_v4_models_pagination_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


