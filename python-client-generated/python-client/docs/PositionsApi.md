# openapi_client.PositionsApi

All URIs are relative to *https://ext-api.vasttrafik.se/pr/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**positions_get**](PositionsApi.md#positions_get) | **GET** /positions | Returns journey positions within a bounding box


# **positions_get**
> List[VTApiPlaneraResaWebV4ModelsPositionsJourneyPositionApiModel] positions_get(lower_left_lat, lower_left_long, upper_right_lat, upper_right_long, transport_modes=transport_modes, details_references=details_references, line_designations=line_designations, limit=limit)

Returns journey positions within a bounding box

Sample request:        GET /positions?lowerLeftLat=57.721723&lowerLeftLong=12.011882&upperRightLat=57.737549&upperRightLong=12.039268&limit=100

### Example

* OAuth Authentication (auth):
```python
import time
import os
import openapi_client
from openapi_client.models.vt_api_planera_resa_core_models_position_transport_mode import VTApiPlaneraResaCoreModelsPositionTransportMode
from openapi_client.models.vt_api_planera_resa_web_v4_models_positions_journey_position_api_model import VTApiPlaneraResaWebV4ModelsPositionsJourneyPositionApiModel
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ext-api.vasttrafik.se/pr/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://ext-api.vasttrafik.se/pr/v4"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PositionsApi(api_client)
    lower_left_lat = 3.4 # float | Lower left latitude of bounding box.
    lower_left_long = 3.4 # float | Lower left longitude of bounding box.
    upper_right_lat = 3.4 # float | Upper right latitude of bounding box.
    upper_right_long = 3.4 # float | Upper right longitude of bounding box.
    transport_modes = [openapi_client.VTApiPlaneraResaCoreModelsPositionTransportMode()] # List[VTApiPlaneraResaCoreModelsPositionTransportMode] | The transport modes to include when searching for journeys, if none specified all transport modes are included. (optional)
    details_references = ['details_references_example'] # List[str] | Filter journeys by one or more journey details reference. (optional)
    line_designations = ['line_designations_example'] # List[str] | Only journeys running the given lineDesignations (case sensitive) are part of the result. (optional)
    limit = 100 # int | Maximum number of journeys in response. Range from 1 to 200. Defaults to 100 (optional) (default to 100)

    try:
        # Returns journey positions within a bounding box
        api_response = api_instance.positions_get(lower_left_lat, lower_left_long, upper_right_lat, upper_right_long, transport_modes=transport_modes, details_references=details_references, line_designations=line_designations, limit=limit)
        print("The response of PositionsApi->positions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->positions_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_left_lat** | **float**| Lower left latitude of bounding box. | 
 **lower_left_long** | **float**| Lower left longitude of bounding box. | 
 **upper_right_lat** | **float**| Upper right latitude of bounding box. | 
 **upper_right_long** | **float**| Upper right longitude of bounding box. | 
 **transport_modes** | [**List[VTApiPlaneraResaCoreModelsPositionTransportMode]**](VTApiPlaneraResaCoreModelsPositionTransportMode.md)| The transport modes to include when searching for journeys, if none specified all transport modes are included. | [optional] 
 **details_references** | [**List[str]**](str.md)| Filter journeys by one or more journey details reference. | [optional] 
 **line_designations** | [**List[str]**](str.md)| Only journeys running the given lineDesignations (case sensitive) are part of the result. | [optional] 
 **limit** | **int**| Maximum number of journeys in response. Range from 1 to 200. Defaults to 100 | [optional] [default to 100]

### Return type

[**List[VTApiPlaneraResaWebV4ModelsPositionsJourneyPositionApiModel]**](VTApiPlaneraResaWebV4ModelsPositionsJourneyPositionApiModel.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the search was successfully completed. |  -  |
**400** | If any of the search parameters were invalid.&lt;br /&gt;              The following error codes can be returned:              1004: Corrupt details reference              5001: Bad service request              7001: Limit must be greater than zero and not greater than 200              7002: All four coordinates of the bounding box must be set |  -  |
**500** | If an internal server error occurred. |  -  |
**503** | If the service is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

