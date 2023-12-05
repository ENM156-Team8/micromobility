# VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel

Detailed information about a journey.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**departure_access_link** | [**VTApiPlaneraResaWebV4ModelsJourneyDetailsDepartureAccessLinkApiModel**](VTApiPlaneraResaWebV4ModelsJourneyDetailsDepartureAccessLinkApiModel.md) |  | [optional] 
**trip_legs** | [**List[VTApiPlaneraResaWebV4ModelsJourneyDetailsTripLegDetailsApiModel]**](VTApiPlaneraResaWebV4ModelsJourneyDetailsTripLegDetailsApiModel.md) | Detailed information, including stops, about the trip legs. | [optional] 
**connection_links** | [**List[VTApiPlaneraResaWebV4ModelsJourneyDetailsConnectionLinkApiModel]**](VTApiPlaneraResaWebV4ModelsJourneyDetailsConnectionLinkApiModel.md) | A list of ConnectionLinks between TripLegs, when applicable. The internal order of TripLegs and ConnectionLinks is defined by Index-property on the objects. | [optional] 
**arrival_access_link** | [**VTApiPlaneraResaWebV4ModelsJourneyDetailsArrivalAccessLinkApiModel**](VTApiPlaneraResaWebV4ModelsJourneyDetailsArrivalAccessLinkApiModel.md) |  | [optional] 
**destination_link** | [**VTApiPlaneraResaWebV4ModelsJourneyDetailsDestinationLinkApiModel**](VTApiPlaneraResaWebV4ModelsJourneyDetailsDestinationLinkApiModel.md) |  | [optional] 
**ticket_suggestions_result** | [**VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionsResultApiModel**](VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionsResultApiModel.md) |  | [optional] 
**tariff_zones** | [**List[VTApiPlaneraResaWebV4ModelsJourneyDetailsTariffZoneApiModel]**](VTApiPlaneraResaWebV4ModelsJourneyDetailsTariffZoneApiModel.md) | The tariff zones that the journey traverses. | [optional] 
**occupancy** | [**VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel**](VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_journey_details_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journey_details_journey_details_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journey_details_journey_details_api_model_dict = vt_api_planera_resa_web_v4_models_journey_details_journey_details_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel from a dict
vt_api_planera_resa_web_v4_models_journey_details_journey_details_api_model_form_dict = vt_api_planera_resa_web_v4_models_journey_details_journey_details_api_model.from_dict(vt_api_planera_resa_web_v4_models_journey_details_journey_details_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


