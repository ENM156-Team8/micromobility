# VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyDetailsApiModel

Information about a service journey.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | 16-digit Västtrafik service journey gid. | [optional] 
**direction** | **str** | A description of the direction. | [optional] 
**line** | [**VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineDetailsApiModel**](VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineDetailsApiModel.md) |  | [optional] 
**service_journey_coordinates** | [**List[VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsCoordinateApiModel]**](VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsCoordinateApiModel.md) | The coordinates of the service journey. | [optional] 
**calls_on_service_journey** | [**List[VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsCallDetailsApiModel]**](VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsCallDetailsApiModel.md) | All calls on the service journey. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_details_api_model import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyDetailsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyDetailsApiModel from a JSON string
vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_details_api_model_instance = VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyDetailsApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyDetailsApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_details_api_model_dict = vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_details_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyDetailsApiModel from a dict
vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_details_api_model_form_dict = vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_details_api_model.from_dict(vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_details_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


