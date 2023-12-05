# VTApiPlaneraResaWebV4ModelsJourneyDetailsLineDetailsApiModel

Information about a line.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The line name. | [optional] 
**background_color** | **str** | The background color of the line symbol. | [optional] 
**foreground_color** | **str** | The foreground color of the line symbol. | [optional] 
**border_color** | **str** | The border color of the line symbol. | [optional] 
**transport_mode** | [**VTApiPlaneraResaCoreModelsTransportMode**](VTApiPlaneraResaCoreModelsTransportMode.md) |  | [optional] 
**transport_sub_mode** | [**VTApiPlaneraResaCoreModelsTransportSubMode**](VTApiPlaneraResaCoreModelsTransportSubMode.md) |  | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_line_details_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsLineDetailsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsLineDetailsApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journey_details_line_details_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneyDetailsLineDetailsApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneyDetailsLineDetailsApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journey_details_line_details_api_model_dict = vt_api_planera_resa_web_v4_models_journey_details_line_details_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsLineDetailsApiModel from a dict
vt_api_planera_resa_web_v4_models_journey_details_line_details_api_model_form_dict = vt_api_planera_resa_web_v4_models_journey_details_line_details_api_model.from_dict(vt_api_planera_resa_web_v4_models_journey_details_line_details_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


