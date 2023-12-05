# VTApiPlaneraResaWebV4ModelsJourneyDetailsStopAreaApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | The 16-digit Västtrafik gid of the stop area. | [optional] 
**name** | **str** | The stop area name. | [optional] 
**latitude** | **float** | The latitude of the stop point. | [optional] 
**longitude** | **float** | The longitude of the stop point. | [optional] 
**tariff_zone1** | [**VTApiPlaneraResaWebV4ModelsJourneyDetailsTariffZoneApiModel**](VTApiPlaneraResaWebV4ModelsJourneyDetailsTariffZoneApiModel.md) |  | [optional] 
**tariff_zone2** | [**VTApiPlaneraResaWebV4ModelsJourneyDetailsTariffZoneApiModel**](VTApiPlaneraResaWebV4ModelsJourneyDetailsTariffZoneApiModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_stop_area_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsStopAreaApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsStopAreaApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journey_details_stop_area_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneyDetailsStopAreaApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneyDetailsStopAreaApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journey_details_stop_area_api_model_dict = vt_api_planera_resa_web_v4_models_journey_details_stop_area_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsStopAreaApiModel from a dict
vt_api_planera_resa_web_v4_models_journey_details_stop_area_api_model_form_dict = vt_api_planera_resa_web_v4_models_journey_details_stop_area_api_model.from_dict(vt_api_planera_resa_web_v4_models_journey_details_stop_area_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


