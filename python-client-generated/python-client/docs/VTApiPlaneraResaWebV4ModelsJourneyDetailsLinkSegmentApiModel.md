# VTApiPlaneraResaWebV4ModelsJourneyDetailsLinkSegmentApiModel

Represents a segment of a departure access link, arrival access link or destination link.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Segment name. | [optional] 
**maneuver** | [**VTApiPlaneraResaWebV4ModelsLinkSegmentManeuver**](VTApiPlaneraResaWebV4ModelsLinkSegmentManeuver.md) |  | [optional] 
**orientation** | [**VTApiPlaneraResaWebV4ModelsLinkSegmentOrientation**](VTApiPlaneraResaWebV4ModelsLinkSegmentOrientation.md) |  | [optional] 
**maneuver_description** | **str** | Description for the maneuver. | [optional] 
**distance_in_meters** | **int** | Distance for this segment in meter. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_link_segment_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsLinkSegmentApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsLinkSegmentApiModel from a JSON string
vt_api_planera_resa_web_v4_models_journey_details_link_segment_api_model_instance = VTApiPlaneraResaWebV4ModelsJourneyDetailsLinkSegmentApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsJourneyDetailsLinkSegmentApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_journey_details_link_segment_api_model_dict = vt_api_planera_resa_web_v4_models_journey_details_link_segment_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsJourneyDetailsLinkSegmentApiModel from a dict
vt_api_planera_resa_web_v4_models_journey_details_link_segment_api_model_form_dict = vt_api_planera_resa_web_v4_models_journey_details_link_segment_api_model.from_dict(vt_api_planera_resa_web_v4_models_journey_details_link_segment_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


