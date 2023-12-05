# VTApiPlaneraResaWebV4ModelsJourneyDetailsServiceJourneyApiModel

Information about a service journey.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | 16-digit Västtrafik service journey gid that the trip leg is a part of. | [optional] 
**direction** | **str** | A description of the direction. | [optional] 
**line** | [**VTApiPlaneraResaWebV4ModelsJourneyDetailsLineDetailsApiModel**](VTApiPlaneraResaWebV4ModelsJourneyDetailsLineDetailsApiModel.md) |  | [optional] 
**service_journey_coordinates** | [**List[VTApiPlaneraResaWebV4ModelsCoordinateApiModel]**](VTApiPlaneraResaWebV4ModelsCoordinateApiModel.md) | The coordinates on the service journey. | [optional] 
**calls_on_service_journey** | [**List[VTApiPlaneraResaWebV4ModelsJourneyDetailsCallDetailsApiModel]**](VTApiPlaneraResaWebV4ModelsJourneyDetailsCallDetailsApiModel.md) | All calls on the service journey. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_service_journey_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsServiceJourneyApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsServiceJourneyApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journey_details_service_journey_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneyDetailsServiceJourneyApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneyDetailsServiceJourneyApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journey_details_service_journey_api_model_dict = vt_api_planera_resa_web_v4_models_journey_details_service_journey_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsServiceJourneyApiModel from a dict
vt_api_planera_resa_web_v4_models_journey_details_service_journey_api_model_form_dict = vt_api_planera_resa_web_v4_models_journey_details_service_journey_api_model.from_dict(vt_api_planera_resa_web_v4_models_journey_details_service_journey_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


