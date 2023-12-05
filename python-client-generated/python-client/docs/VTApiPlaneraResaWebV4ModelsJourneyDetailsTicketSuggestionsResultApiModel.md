# VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionsResultApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_error** | **bool** | Flag indicating that an error occurred while getting ticket suggestions. | [optional] 
**ticket_suggestions** | [**List[VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionApiModel]**](VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionApiModel.md) | Ticket suggestions for a journey. | [optional] 
**ticket_validities** | [**List[VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel]**](VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel.md) | An array with the tickets from the existingTickets-array in the post-body. Validity for the journey is indicated for each ticket in the array. Included if &#39;ticketsuggestions&#39; is passed in the includes array in the request, otherwise null. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestions_result_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionsResultApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionsResultApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestions_result_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionsResultApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionsResultApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestions_result_api_model_dict = vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestions_result_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionsResultApiModel from a dict
vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestions_result_api_model_form_dict = vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestions_result_api_model.from_dict(vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestions_result_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


