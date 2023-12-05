# VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionApiModel

Information about a ticket suggestion.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** | The product id. | [optional] 
**product_name** | **str** | The product name. | [optional] 
**product_type** | **int** | The product type. | [optional] 
**traveller_category** | [**VTApiPlaneraResaCoreModelsTravellerCategory**](VTApiPlaneraResaCoreModelsTravellerCategory.md) |  | [optional] 
**price_in_sek** | **float** | The product price in SEK. | [optional] 
**time_validity** | [**VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel**](VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel.md) |  | [optional] 
**time_limitation** | [**VTApiPlaneraResaCoreModelsTimeLimitation**](VTApiPlaneraResaCoreModelsTimeLimitation.md) |  | [optional] 
**sale_channels** | [**List[VTApiPlaneraResaWebV4ModelsJourneyDetailsChannelApiModel]**](VTApiPlaneraResaWebV4ModelsJourneyDetailsChannelApiModel.md) | A list of the channels that sell the product. | [optional] 
**valid_zones** | [**List[VTApiPlaneraResaWebV4ModelsJourneyDetailsZoneApiModel]**](VTApiPlaneraResaWebV4ModelsJourneyDetailsZoneApiModel.md) | A list of the valid zones for the ticket. | [optional] 
**product_instance_type** | [**VTApiPlaneraResaWebV4ModelsProductInstanceTypeApiModel**](VTApiPlaneraResaWebV4ModelsProductInstanceTypeApiModel.md) |  | [optional] 
**punch_configuration** | [**VTApiPlaneraResaWebV4ModelsJourneyDetailsPunchConfigurationApiModel**](VTApiPlaneraResaWebV4ModelsJourneyDetailsPunchConfigurationApiModel.md) |  | [optional] 
**offer_specification** | **str** | Used to get ticket offer. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestion_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestion_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestion_api_model_dict = vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestion_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionApiModel from a dict
vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestion_api_model_form_dict = vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestion_api_model.from_dict(vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestion_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


