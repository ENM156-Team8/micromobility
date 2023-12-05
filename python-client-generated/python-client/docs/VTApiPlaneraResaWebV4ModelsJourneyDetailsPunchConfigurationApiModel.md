# VTApiPlaneraResaWebV4ModelsJourneyDetailsPunchConfigurationApiModel

Represents punch configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quota** | **int** | Punch quota of a single ticket. | [optional] 
**duration** | [**VTApiPlaneraResaWebV4ModelsJourneyDetailsPunchConfigurationDurationApiModel**](VTApiPlaneraResaWebV4ModelsJourneyDetailsPunchConfigurationDurationApiModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_punch_configuration_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsPunchConfigurationApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsPunchConfigurationApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journey_details_punch_configuration_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneyDetailsPunchConfigurationApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneyDetailsPunchConfigurationApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journey_details_punch_configuration_api_model_dict = vt_api_planera_resa_web_v4_models_journey_details_punch_configuration_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsPunchConfigurationApiModel from a dict
vt_api_planera_resa_web_v4_models_journey_details_punch_configuration_api_model_form_dict = vt_api_planera_resa_web_v4_models_journey_details_punch_configuration_api_model.from_dict(vt_api_planera_resa_web_v4_models_journey_details_punch_configuration_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


