# VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyApiModel

Information about a service journey of a departure or arrival.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | 16-digit Västtrafik service journey gid. | 
**origin** | **str** | A description of the origin. | [optional] 
**direction** | **str** | A description of the direction. | [optional] 
**line** | [**VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineApiModel**](VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineApiModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_api_model import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyApiModel from a JSON string
vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_api_model_instance = VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_api_model_dict = vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyApiModel from a dict
vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_api_model_form_dict = vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_api_model.from_dict(vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


