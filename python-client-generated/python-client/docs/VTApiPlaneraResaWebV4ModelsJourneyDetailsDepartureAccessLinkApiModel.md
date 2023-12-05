# VTApiPlaneraResaWebV4ModelsJourneyDetailsDepartureAccessLinkApiModel

Information about a walk, bike or car link from origin to first public transport trip leg.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport_mode** | [**VTApiPlaneraResaCoreModelsTransportMode**](VTApiPlaneraResaCoreModelsTransportMode.md) |  | [optional] 
**transport_sub_mode** | [**VTApiPlaneraResaCoreModelsTransportSubMode**](VTApiPlaneraResaCoreModelsTransportSubMode.md) |  | [optional] 
**origin** | [**VTApiPlaneraResaWebV4ModelsJourneyDetailsLinkEndpointApiModel**](VTApiPlaneraResaWebV4ModelsJourneyDetailsLinkEndpointApiModel.md) |  | [optional] 
**destination** | [**VTApiPlaneraResaWebV4ModelsJourneyDetailsCallApiModel**](VTApiPlaneraResaWebV4ModelsJourneyDetailsCallApiModel.md) |  | [optional] 
**notes** | [**List[VTApiPlaneraResaCoreModelsNote]**](VTApiPlaneraResaCoreModelsNote.md) | An ordered list (most important first) of notes related to the access link. | [optional] 
**distance_in_meters** | **int** | Distance in meters. | [optional] 
**planned_departure_time** | **str** | The planned departure time in RFC 3339 format. | [optional] 
**planned_arrival_time** | **str** | The planned arrival time in RFC 3339 format. | [optional] 
**planned_duration_in_minutes** | **int** | The planned duration in minutes. | [optional] 
**estimated_departure_time** | **str** | The estimated departure time in RFC 3339 format, if available. | [optional] 
**estimated_arrival_time** | **str** | The estimated arrival time in RFC 3339 format, if available. | [optional] 
**estimated_duration_in_minutes** | **int** | The estimated duration in minutes, if available. | [optional] 
**estimated_number_of_steps** | **int** | Number of steps based on the distance and an estimated step length of 0.65 meters. | [optional] 
**link_coordinates** | [**List[VTApiPlaneraResaWebV4ModelsCoordinateApiModel]**](VTApiPlaneraResaWebV4ModelsCoordinateApiModel.md) | The coordinates for the link. | [optional] 
**segments** | [**List[VTApiPlaneraResaWebV4ModelsJourneyDetailsLinkSegmentApiModel]**](VTApiPlaneraResaWebV4ModelsJourneyDetailsLinkSegmentApiModel.md) | The segments that make up this link. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_departure_access_link_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsDepartureAccessLinkApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsDepartureAccessLinkApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journey_details_departure_access_link_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneyDetailsDepartureAccessLinkApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneyDetailsDepartureAccessLinkApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journey_details_departure_access_link_api_model_dict = vt_api_planera_resa_web_v4_models_journey_details_departure_access_link_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsDepartureAccessLinkApiModel from a dict
vt_api_planera_resa_web_v4_models_journey_details_departure_access_link_api_model_form_dict = vt_api_planera_resa_web_v4_models_journey_details_departure_access_link_api_model.from_dict(vt_api_planera_resa_web_v4_models_journey_details_departure_access_link_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


