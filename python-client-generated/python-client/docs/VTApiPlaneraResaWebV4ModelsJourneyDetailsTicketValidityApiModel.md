# VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel

Information about ticket validity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ticket id. | [optional] 
**is_valid_for_journey** | **bool** | Indicates if the ticket is valid for the journey. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_ticket_validity_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journey_details_ticket_validity_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journey_details_ticket_validity_api_model_dict = vt_api_planera_resa_web_v4_models_journey_details_ticket_validity_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel from a dict
vt_api_planera_resa_web_v4_models_journey_details_ticket_validity_api_model_form_dict = vt_api_planera_resa_web_v4_models_journey_details_ticket_validity_api_model.from_dict(vt_api_planera_resa_web_v4_models_journey_details_ticket_validity_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


