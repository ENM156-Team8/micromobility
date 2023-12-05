# VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel

Information about a journey.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reconstruction_reference** | **str** | A reference that can be used to reconstruct this journey at a later time. | [optional] 
**details_reference** | **str** | A reference that should be used when getting detailed information about the journey. | [optional] 
**departure_access_link** | [**VTApiPlaneraResaWebV4ModelsJourneysDepartureAccessLinkApiModel**](VTApiPlaneraResaWebV4ModelsJourneysDepartureAccessLinkApiModel.md) |  | [optional] 
**trip_legs** | [**List[VTApiPlaneraResaWebV4ModelsJourneysTripLegApiModel]**](VTApiPlaneraResaWebV4ModelsJourneysTripLegApiModel.md) | A list of trip legs on a journey, when applicable. A journey has either one or more trip legs or one  destination link. | [optional] 
**connection_links** | [**List[VTApiPlaneraResaWebV4ModelsJourneysConnectionLinkApiModel]**](VTApiPlaneraResaWebV4ModelsJourneysConnectionLinkApiModel.md) | A list of ConnectionLinks between TripLegs, when applicable. The internal order of TripLegs and ConnectionLinks is defined by Index-property on the objects. | [optional] 
**arrival_access_link** | [**VTApiPlaneraResaWebV4ModelsJourneysArrivalAccessLinkApiModel**](VTApiPlaneraResaWebV4ModelsJourneysArrivalAccessLinkApiModel.md) |  | [optional] 
**destination_link** | [**VTApiPlaneraResaWebV4ModelsJourneysDestinationLinkApiModel**](VTApiPlaneraResaWebV4ModelsJourneysDestinationLinkApiModel.md) |  | [optional] 
**is_departed** | **bool** | Flag indicating if the first trip leg of the journey is departed. | [optional] 
**occupancy** | [**VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel**](VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journeys_journey_api_model import VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journeys_journey_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journeys_journey_api_model_dict = vt_api_planera_resa_web_v4_models_journeys_journey_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel from a dict
vt_api_planera_resa_web_v4_models_journeys_journey_api_model_form_dict = vt_api_planera_resa_web_v4_models_journeys_journey_api_model.from_dict(vt_api_planera_resa_web_v4_models_journeys_journey_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


