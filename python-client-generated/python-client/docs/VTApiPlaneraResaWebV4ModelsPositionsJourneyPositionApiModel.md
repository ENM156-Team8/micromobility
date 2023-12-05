# VTApiPlaneraResaWebV4ModelsPositionsJourneyPositionApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details_reference** | **str** | Journey reference | [optional] 
**line** | [**VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel**](VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.md) |  | [optional] 
**notes** | [**List[VTApiPlaneraResaCoreModelsNote]**](VTApiPlaneraResaCoreModelsNote.md) | Journey notes | [optional] 
**name** | **str** | Journey name | [optional] 
**direction** | **str** | Journey direction | [optional] 
**latitude** | **float** | Current latitude of journey | [optional] 
**longitude** | **float** | Current longitude of journey | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_positions_journey_position_api_model import VTApiPlaneraResaWebV4ModelsPositionsJourneyPositionApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsPositionsJourneyPositionApiModel from a JSON string
vt_api_planera_resa_web_v4_models_positions_journey_position_api_model_instance = VTApiPlaneraResaWebV4ModelsPositionsJourneyPositionApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsPositionsJourneyPositionApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_positions_journey_position_api_model_dict = vt_api_planera_resa_web_v4_models_positions_journey_position_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsPositionsJourneyPositionApiModel from a dict
vt_api_planera_resa_web_v4_models_positions_journey_position_api_model_form_dict = vt_api_planera_resa_web_v4_models_positions_journey_position_api_model.from_dict(vt_api_planera_resa_web_v4_models_positions_journey_position_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


