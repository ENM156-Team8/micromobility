# VTApiPlaneraResaWebV4ModelsJourneysTripLegApiModel

Information about a journey trip leg.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin** | [**VTApiPlaneraResaWebV4ModelsJourneysCallApiModel**](VTApiPlaneraResaWebV4ModelsJourneysCallApiModel.md) |  | 
**destination** | [**VTApiPlaneraResaWebV4ModelsJourneysCallApiModel**](VTApiPlaneraResaWebV4ModelsJourneysCallApiModel.md) |  | 
**is_cancelled** | **bool** | Flag indicating if the trip leg is cancelled. | 
**is_part_cancelled** | **bool** | Flag indicating if the trip leg is partially cancelled. | [optional] 
**service_journey** | [**VTApiPlaneraResaWebV4ModelsJourneysServiceJourneyApiModel**](VTApiPlaneraResaWebV4ModelsJourneysServiceJourneyApiModel.md) |  | [optional] 
**notes** | [**List[VTApiPlaneraResaCoreModelsNote]**](VTApiPlaneraResaCoreModelsNote.md) | An ordered list (most important first) of notes related to the trip leg. | [optional] 
**estimated_distance_in_meters** | **int** | Estimated distance in meters. Only for transport mode Walk. | [optional] 
**planned_connecting_time_in_minutes** | **int** | The planned (according to timetable) connecting time in minutes relative to  the previous public transport trip leg (if any). | [optional] 
**estimated_connecting_time_in_minutes** | **int** | The estimated (according to real-time data) connecting time in minutes relative to  the previous public transport trip leg (if any). | [optional] 
**is_risk_of_missing_connection** | **bool** | Flag indicating that there is less than 5 minutes margin between arriving at the  origin stop point and the departure from that stop point. | [optional] 
**planned_departure_time** | **str** | The planned departure time in RFC 3339 format. | [optional] 
**planned_arrival_time** | **str** | The planned arrival time in RFC 3339 format. | [optional] 
**planned_duration_in_minutes** | **int** | The planned duration in minutes. | [optional] 
**estimated_departure_time** | **str** | The estimated departure time in RFC 3339 format, if available. | [optional] 
**estimated_arrival_time** | **str** | The estimated arrival time in RFC 3339 format, if available. | [optional] 
**estimated_duration_in_minutes** | **int** | The estimated duration in minutes, if available. | [optional] 
**estimated_otherwise_planned_arrival_time** | **str** | The best known time of the arrival in RFC 3339 format. Is EstimatedArrivalTime if exists, otherwise PlannedArrivalTime. | [optional] [readonly] 
**estimated_otherwise_planned_departure_time** | **str** | The best known time of the departure in RFC 3339 format. Is EstimatedDepartureTime if exists, otherwise PlannedDepartureTime. | [optional] [readonly] 
**occupancy** | [**VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel**](VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel.md) |  | [optional] 
**journey_leg_index** | **int** | Index of Leg in Journey | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journeys_trip_leg_api_model import VTApiPlaneraResaWebV4ModelsJourneysTripLegApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneysTripLegApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journeys_trip_leg_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneysTripLegApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneysTripLegApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journeys_trip_leg_api_model_dict = vt_api_planera_resa_web_v4_models_journeys_trip_leg_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneysTripLegApiModel from a dict
vt_api_planera_resa_web_v4_models_journeys_trip_leg_api_model_form_dict = vt_api_planera_resa_web_v4_models_journeys_trip_leg_api_model.from_dict(vt_api_planera_resa_web_v4_models_journeys_trip_leg_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


