# VTApiPlaneraResaWebV4ModelsJourneyDetailsChannelApiModel

Information about a channel related to the ticket suggestion.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The channel id. | [optional] 
**ticket_name** | **str** | The channel-specific ticket name, set if the channel is configured to override the default  product name. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_channel_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsChannelApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsChannelApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journey_details_channel_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneyDetailsChannelApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneyDetailsChannelApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journey_details_channel_api_model_dict = vt_api_planera_resa_web_v4_models_journey_details_channel_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsChannelApiModel from a dict
vt_api_planera_resa_web_v4_models_journey_details_channel_api_model_form_dict = vt_api_planera_resa_web_v4_models_journey_details_channel_api_model.from_dict(vt_api_planera_resa_web_v4_models_journey_details_channel_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


