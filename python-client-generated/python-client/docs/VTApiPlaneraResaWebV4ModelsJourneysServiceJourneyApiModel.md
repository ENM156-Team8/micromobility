# VTApiPlaneraResaWebV4ModelsJourneysServiceJourneyApiModel

Information about a service journey of a departure or arrival.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | 16-digit Västtrafik service journey gid. | 
**direction** | **str** | A description of the direction. | [optional] 
**number** | **str** | Västtrafik service journey number that the trip leg is a part of. | [optional] 
**line** | [**VTApiPlaneraResaWebV4ModelsJourneysLineApiModel**](VTApiPlaneraResaWebV4ModelsJourneysLineApiModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journeys_service_journey_api_model import VTApiPlaneraResaWebV4ModelsJourneysServiceJourneyApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneysServiceJourneyApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journeys_service_journey_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneysServiceJourneyApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneysServiceJourneyApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journeys_service_journey_api_model_dict = vt_api_planera_resa_web_v4_models_journeys_service_journey_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneysServiceJourneyApiModel from a dict
vt_api_planera_resa_web_v4_models_journeys_service_journey_api_model_form_dict = vt_api_planera_resa_web_v4_models_journeys_service_journey_api_model.from_dict(vt_api_planera_resa_web_v4_models_journeys_service_journey_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


