# VTApiPlaneraResaWebV4ModelsJourneysGetJourneysResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel]**](VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel.md) | The results. | [optional] 
**pagination** | [**VTApiPlaneraResaWebV4ModelsPaginationProperties**](VTApiPlaneraResaWebV4ModelsPaginationProperties.md) |  | [optional] 
**links** | [**VTApiPlaneraResaWebV4ModelsPaginationLinks**](VTApiPlaneraResaWebV4ModelsPaginationLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journeys_get_journeys_response import VTApiPlaneraResaWebV4ModelsJourneysGetJourneysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneysGetJourneysResponse from a JSON string
vt_api_planera_resa_web_v4_models_journeys_get_journeys_response_instance = VTApiPlaneraResaWebV4ModelsJourneysGetJourneysResponse.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneysGetJourneysResponse.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journeys_get_journeys_response_dict = vt_api_planera_resa_web_v4_models_journeys_get_journeys_response_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneysGetJourneysResponse from a dict
vt_api_planera_resa_web_v4_models_journeys_get_journeys_response_form_dict = vt_api_planera_resa_web_v4_models_journeys_get_journeys_response.from_dict(vt_api_planera_resa_web_v4_models_journeys_get_journeys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


