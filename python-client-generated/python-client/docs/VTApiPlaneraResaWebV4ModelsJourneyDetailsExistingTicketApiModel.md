# VTApiPlaneraResaWebV4ModelsJourneyDetailsExistingTicketApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An Id for matching this existingTicket with ticketValidityApiModel in response. | [optional] 
**offer_specification** | **str** | From TicketSuggestionApiModel | [optional] 
**time_of_issue** | **str** | Must be specified in RFC 3339 format | [optional] 
**time_of_activation** | **str** | Must be specified in RFC 3339 format | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_existing_ticket_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsExistingTicketApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsExistingTicketApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journey_details_existing_ticket_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneyDetailsExistingTicketApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneyDetailsExistingTicketApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journey_details_existing_ticket_api_model_dict = vt_api_planera_resa_web_v4_models_journey_details_existing_ticket_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsExistingTicketApiModel from a dict
vt_api_planera_resa_web_v4_models_journey_details_existing_ticket_api_model_form_dict = vt_api_planera_resa_web_v4_models_journey_details_existing_ticket_api_model.from_dict(vt_api_planera_resa_web_v4_models_journey_details_existing_ticket_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


