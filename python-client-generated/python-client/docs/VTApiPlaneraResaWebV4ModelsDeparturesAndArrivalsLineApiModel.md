# VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineApiModel

Information about a line of a departure or arrival service journey.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | 16-digit Västtrafik line gid. | [optional] 
**name** | **str** | The line name. | [optional] 
**short_name** | **str** | The short name of the line, usually 5 characters or less. | [optional] 
**designation** | **str** | The designation of the line. | [optional] 
**background_color** | **str** | The background color of the line symbol. | [optional] 
**foreground_color** | **str** | The foreground color of the line symbol. | [optional] 
**border_color** | **str** | The border color of the line symbol. | [optional] 
**transport_mode** | [**VTApiPlaneraResaCoreModelsTransportMode**](VTApiPlaneraResaCoreModelsTransportMode.md) |  | [optional] 
**transport_sub_mode** | [**VTApiPlaneraResaCoreModelsTransportSubMode**](VTApiPlaneraResaCoreModelsTransportSubMode.md) |  | [optional] 
**is_wheelchair_accessible** | **bool** | Flag indicating if the line is wheelchair accessible. | [optional] 

## Example

```python
from openapi_client.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_line_api_model import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineApiModel from a JSON string
vt_api_planera_resa_web_v4_models_departures_and_arrivals_line_api_model_instance = VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineApiModel.from_json(json)
# print the JSON string representation of the object
print VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineApiModel.to_json()

# convert the object into a dict
vt_api_planera_resa_web_v4_models_departures_and_arrivals_line_api_model_dict = vt_api_planera_resa_web_v4_models_departures_and_arrivals_line_api_model_instance.to_dict()
# create an instance of VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineApiModel from a dict
vt_api_planera_resa_web_v4_models_departures_and_arrivals_line_api_model_form_dict = vt_api_planera_resa_web_v4_models_departures_and_arrivals_line_api_model.from_dict(vt_api_planera_resa_web_v4_models_departures_and_arrivals_line_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


