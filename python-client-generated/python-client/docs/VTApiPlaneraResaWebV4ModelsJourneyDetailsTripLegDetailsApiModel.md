# VTApiPlaneraResaWebV4ModelsJourneyDetailsTripLegDetailsApiModel

Detailed information about a Public Transport trip leg.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_journeys** | [**List[VTApiPlaneraResaWebV4ModelsJourneyDetailsServiceJourneyApiModel]**](VTApiPlaneraResaWebV4ModelsJourneyDetailsServiceJourneyApiModel.md) | The service journey for the trip leg. | [optional] 
**calls_on_trip_leg** | [**List[VTApiPlaneraResaWebV4ModelsJourneyDetailsCallDetailsApiModel]**](VTApiPlaneraResaWebV4ModelsJourneyDetailsCallDetailsApiModel.md) | The calls on the trip leg. | [optional] 
**trip_leg_coordinates** | [**List[VTApiPlaneraResaWebV4ModelsCoordinateApiModel]**](VTApiPlaneraResaWebV4ModelsCoordinateApiModel.md) | The coordinates for the trip leg. | [optional] 
**tariff_zones** | [**List[VTApiPlaneraResaWebV4ModelsJourneyDetailsTariffZoneApiModel]**](VTApiPlaneraResaWebV4ModelsJourneyDetailsTariffZoneApiModel.md) | The tariff zones that the trip leg traverses. | [optional] 
**is_cancelled** | **bool** | Flag indicating if the trip leg is cancelled. | [optional] 
**is_part_cancelled** | **bool** | Flag indicating if the trip leg is partially cancelled. | [optional] 
**occupancy** | [**VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel**](VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel.md) |  | [optional] 
**journey_leg_index** | **int** | Index of Leg in Journey | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_trip_leg_details_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsTripLegDetailsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsTripLegDetailsApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journey_details_trip_leg_details_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneyDetailsTripLegDetailsApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneyDetailsTripLegDetailsApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journey_details_trip_leg_details_api_model_dict = vt_api_planera_resa_web_v4_models_journey_details_trip_leg_details_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsTripLegDetailsApiModel from a dict
vt_api_planera_resa_web_v4_models_journey_details_trip_leg_details_api_model_form_dict = vt_api_planera_resa_web_v4_models_journey_details_trip_leg_details_api_model.from_dict(vt_api_planera_resa_web_v4_models_journey_details_trip_leg_details_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


