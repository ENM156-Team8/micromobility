# VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details_reference** | **str** | A reference that should be used when getting detailed information about the journey. | [optional] 
**service_journey** | [**VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyApiModel**](VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyApiModel.md) |  | [optional] 
**stop_point** | [**VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsStopPointApiModel**](VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsStopPointApiModel.md) |  | 
**planned_time** | **str** | The planned time of the call in RFC 3339 format. | 
**estimated_time** | **str** | The estimated time of the call in RFC 3339 format. | [optional] 
**estimated_otherwise_planned_time** | **str** | The best known time of the call in RFC 3339 format. Is EstimatedTime if exists, otherwise PlannedTime. | [optional] [readonly] 
**is_cancelled** | **bool** | Flag indicating if the departure or arrival is cancelled. | [optional] 
**is_part_cancelled** | **bool** | Flag indicating if the departure or arrival is partially cancelled. | [optional] 
**occupancy** | [**VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel**](VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_departure_api_model import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureApiModel from a JSON string
vt_api_planera_resa_web_v4_models_departures_and_arrivals_departure_api_model_instance = VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_departures_and_arrivals_departure_api_model_dict = vt_api_planera_resa_web_v4_models_departures_and_arrivals_departure_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureApiModel from a dict
vt_api_planera_resa_web_v4_models_departures_and_arrivals_departure_api_model_form_dict = vt_api_planera_resa_web_v4_models_departures_and_arrivals_departure_api_model.from_dict(vt_api_planera_resa_web_v4_models_departures_and_arrivals_departure_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


