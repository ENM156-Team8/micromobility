# VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsCallDetailsApiModel

Information about a call on the trip leg.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stop_point** | [**VTApiPlaneraResaWebV4ModelsJourneyDetailsStopPointApiModel**](VTApiPlaneraResaWebV4ModelsJourneyDetailsStopPointApiModel.md) |  | 
**planned_arrival_time** | **str** | The planned arrival time for the call in RFC 3339 format. | [optional] 
**planned_departure_time** | **str** | The planned departure time for the call in RFC 3339 format. | [optional] 
**estimated_arrival_time** | **str** | The estimated arrival time for the call in RFC 3339 format. | [optional] 
**estimated_departure_time** | **str** | The estimated departure time for the call in RFC 3339 format. | [optional] 
**estimated_otherwise_planned_arrival_time** | **str** | The best known time of the call in RFC 3339 format. Is EstimatedArrivalTime if exists, otherwise PlannedArrivalTime. | [optional] [readonly] 
**estimated_otherwise_planned_departure_time** | **str** | The best known time of the call in RFC 3339 format. Is EstimatedDepartureTime if exists, otherwise PlannedDepartureTime. | [optional] [readonly] 
**planned_platform** | **str** | The planned platform of the call. | [optional] 
**estimated_platform** | **str** | The estimated platform of the call. | [optional] 
**latitude** | **float** | The latitude of the stop point of the call. | [optional] 
**longitude** | **float** | The longitude of the stop point of the call. | [optional] 
**index** | **str** | The index of the stop point of the call. | [optional] 
**occupancy** | [**VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel**](VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel.md) |  | [optional] 
**is_cancelled** | **bool** | Flag indicating if the call is cancelled. | [optional] 
**is_departure_cancelled** | **bool** | Flag indicating if the departure is cancelled. | [optional] 
**is_arrival_cancelled** | **bool** | Flag indicating if the arrival is cancelled. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_call_details_api_model import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsCallDetailsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsCallDetailsApiModel from a JSON string
vt_api_planera_resa_web_v4_models_departures_and_arrivals_call_details_api_model_instance = VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsCallDetailsApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsCallDetailsApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_departures_and_arrivals_call_details_api_model_dict = vt_api_planera_resa_web_v4_models_departures_and_arrivals_call_details_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsCallDetailsApiModel from a dict
vt_api_planera_resa_web_v4_models_departures_and_arrivals_call_details_api_model_form_dict = vt_api_planera_resa_web_v4_models_departures_and_arrivals_call_details_api_model.from_dict(vt_api_planera_resa_web_v4_models_departures_and_arrivals_call_details_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


