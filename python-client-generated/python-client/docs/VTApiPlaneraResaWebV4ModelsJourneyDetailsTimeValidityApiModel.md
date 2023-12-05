# VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel

Information about the time validity of a ticket suggestion.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**VTApiPlaneraResaCoreModelsTimeValidityType**](VTApiPlaneraResaCoreModelsTimeValidityType.md) |  | [optional] 
**amount** | **int** | The amount of the unit specified by the Unit property. Always used together with the Unit property. | [optional] 
**unit** | [**VTApiPlaneraResaCoreModelsTimeValidityUnit**](VTApiPlaneraResaCoreModelsTimeValidityUnit.md) |  | [optional] 
**from_date** | **str** | The from date of a date interval specified in RFC 3339 format. Always used together with the  ToDate property. | [optional] 
**to_date** | **str** | The to date of a date interval specified in RFC 3339 format. Always used together with the  FromDate property. | [optional] 
**from_date_time** | **str** | The from time of a datetime interval specified in RFC 3339 format. Always used together with  the ToDateTime property. | [optional] 
**to_date_time** | **str** | The to time of a datetime interval specified in RFC 3339 format. Always used together with  the FromDateTime property. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_time_validity_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journey_details_time_validity_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journey_details_time_validity_api_model_dict = vt_api_planera_resa_web_v4_models_journey_details_time_validity_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel from a dict
vt_api_planera_resa_web_v4_models_journey_details_time_validity_api_model_form_dict = vt_api_planera_resa_web_v4_models_journey_details_time_validity_api_model.from_dict(vt_api_planera_resa_web_v4_models_journey_details_time_validity_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


