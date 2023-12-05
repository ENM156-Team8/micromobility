# openapi_client.StopPointsApi

All URIs are relative to *https://ext-api.vasttrafik.se/pr/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stop_points_stop_point_gid_arrivals_details_reference_details_get**](StopPointsApi.md#stop_points_stop_point_gid_arrivals_details_reference_details_get) | **GET** /stop-points/{stopPointGid}/arrivals/{detailsReference}/details | Returns details about an arrival.
[**stop_points_stop_point_gid_arrivals_get**](StopPointsApi.md#stop_points_stop_point_gid_arrivals_get) | **GET** /stop-points/{stopPointGid}/arrivals | Returns arrivals to the specified stop point at the specified time.
[**stop_points_stop_point_gid_departures_details_reference_details_get**](StopPointsApi.md#stop_points_stop_point_gid_departures_details_reference_details_get) | **GET** /stop-points/{stopPointGid}/departures/{detailsReference}/details | Returns details about a departure.
[**stop_points_stop_point_gid_departures_get**](StopPointsApi.md#stop_points_stop_point_gid_departures_get) | **GET** /stop-points/{stopPointGid}/departures | Returns departures from the specified stop point at the specified time.


# **stop_points_stop_point_gid_arrivals_details_reference_details_get**
> VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel stop_points_stop_point_gid_arrivals_details_reference_details_get(details_reference, stop_point_gid, includes=includes)

Returns details about an arrival.

Sample request:        GET /stop-points/9022014001760003/arrivals/{detailsReference}/details?includes=servicejourneycalls

### Example

* OAuth Authentication (auth):
```python
import time
import os
import openapi_client
from openapi_client.models.vt_api_planera_resa_web_v4_models_arrival_details_include_type import VTApiPlaneraResaWebV4ModelsArrivalDetailsIncludeType
from openapi_client.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_arrival_details_api_model import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel
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
    api_instance = openapi_client.StopPointsApi(api_client)
    details_reference = 'details_reference_example' # str | The reference to the service journey, received from the arrivals call. A detailsReference is only valid during the same day as it was generated.
    stop_point_gid = 'stop_point_gid_example' # str | 
    includes = [openapi_client.VTApiPlaneraResaWebV4ModelsArrivalDetailsIncludeType()] # List[VTApiPlaneraResaWebV4ModelsArrivalDetailsIncludeType] | The additional information to include in the response. (optional)

    try:
        # Returns details about an arrival.
        api_response = api_instance.stop_points_stop_point_gid_arrivals_details_reference_details_get(details_reference, stop_point_gid, includes=includes)
        print("The response of StopPointsApi->stop_points_stop_point_gid_arrivals_details_reference_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StopPointsApi->stop_points_stop_point_gid_arrivals_details_reference_details_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details_reference** | **str**| The reference to the service journey, received from the arrivals call. A detailsReference is only valid during the same day as it was generated. | 
 **stop_point_gid** | **str**|  | 
 **includes** | [**List[VTApiPlaneraResaWebV4ModelsArrivalDetailsIncludeType]**](VTApiPlaneraResaWebV4ModelsArrivalDetailsIncludeType.md)| The additional information to include in the response. | [optional] 

### Return type

[**VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel**](VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If service journey details were successfully retrieved. |  -  |
**400** | If any of the search parameters were invalid.&lt;br /&gt;              The following error codes can be returned:              1002: Missing details reference              1004: Corrupt details reference              5001: Bad service request              5003: Service error              6003: Faulty input |  -  |
**404** | If the details about the arrival could not be found. |  -  |
**500** | If an internal server error occurred. |  -  |
**503** | If the service is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_points_stop_point_gid_arrivals_get**
> VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetArrivalsResponse stop_points_stop_point_gid_arrivals_get(stop_point_gid, start_date_time=start_date_time, time_span_in_minutes=time_span_in_minutes, max_arrivals_per_line_and_direction=max_arrivals_per_line_and_direction, limit=limit, offset=offset, direction_gid=direction_gid)

Returns arrivals to the specified stop point at the specified time.

Sample request:        GET /stop-points/9022014001760003/arrivals

### Example

* OAuth Authentication (auth):
```python
import time
import os
import openapi_client
from openapi_client.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_get_arrivals_response import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetArrivalsResponse
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
    api_instance = openapi_client.StopPointsApi(api_client)
    stop_point_gid = 'stop_point_gid_example' # str | The 16-digit Västtrafik gid of the stop point.
    start_date_time = 'start_date_time_example' # str | The start of the time interval for which to get upcoming arrivals. Must be specified in RFC 3339 format or be null which means that the current time on the server is used. (optional)
    time_span_in_minutes = 60 # int | The number of minutes from the start time for which to get upcoming arrivals. Allowed values are between 0 and 1440. (optional) (default to 60)
    max_arrivals_per_line_and_direction = 2 # int | The maximum number of arrivals for a single line in a specific direction. (optional) (default to 2)
    limit = 10 # int | The number of results to return. (optional) (default to 10)
    offset = 0 # int | The zero-based start offset of the pagination. (optional) (default to 0)
    direction_gid = 'direction_gid_example' # str | Filter result by last stop on journey. Must be a 16-digit Västtrafik stop area (optional)

    try:
        # Returns arrivals to the specified stop point at the specified time.
        api_response = api_instance.stop_points_stop_point_gid_arrivals_get(stop_point_gid, start_date_time=start_date_time, time_span_in_minutes=time_span_in_minutes, max_arrivals_per_line_and_direction=max_arrivals_per_line_and_direction, limit=limit, offset=offset, direction_gid=direction_gid)
        print("The response of StopPointsApi->stop_points_stop_point_gid_arrivals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StopPointsApi->stop_points_stop_point_gid_arrivals_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stop_point_gid** | **str**| The 16-digit Västtrafik gid of the stop point. | 
 **start_date_time** | **str**| The start of the time interval for which to get upcoming arrivals. Must be specified in RFC 3339 format or be null which means that the current time on the server is used. | [optional] 
 **time_span_in_minutes** | **int**| The number of minutes from the start time for which to get upcoming arrivals. Allowed values are between 0 and 1440. | [optional] [default to 60]
 **max_arrivals_per_line_and_direction** | **int**| The maximum number of arrivals for a single line in a specific direction. | [optional] [default to 2]
 **limit** | **int**| The number of results to return. | [optional] [default to 10]
 **offset** | **int**| The zero-based start offset of the pagination. | [optional] [default to 0]
 **direction_gid** | **str**| Filter result by last stop on journey. Must be a 16-digit Västtrafik stop area | [optional] 

### Return type

[**VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetArrivalsResponse**](VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetArrivalsResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If arrivals were successfully retrieved. |  -  |
**400** | If the search text, any of the specified types or the pagination properties are invalid.&lt;br /&gt;              The following error codes can be returned:              4201: Invalid limit and offset values              4203: Invalid start datetime              4204: Invalid timespan              4205: Invalid max arrivals per line and direction              4207: Invalid stop point gid              4208: Invalid direction gid              5001: Bad service request |  -  |
**404** | If the stop point was not found. |  -  |
**500** | If an internal server error occurred. |  -  |
**503** | If the service is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_points_stop_point_gid_departures_details_reference_details_get**
> VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureDetailsApiModel stop_points_stop_point_gid_departures_details_reference_details_get(details_reference, stop_point_gid, includes=includes)

Returns details about a departure.

Sample request:        GET /stop-points/9022014001760003/departures/{detailsReference}/details?includes=servicejourneycalls

### Example

* OAuth Authentication (auth):
```python
import time
import os
import openapi_client
from openapi_client.models.vt_api_planera_resa_web_v4_models_departure_details_include_type import VTApiPlaneraResaWebV4ModelsDepartureDetailsIncludeType
from openapi_client.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_departure_details_api_model import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureDetailsApiModel
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
    api_instance = openapi_client.StopPointsApi(api_client)
    details_reference = 'details_reference_example' # str | The reference to the service journey, received from the departures call. A detailsReference is only valid during the same day as it was generated.
    stop_point_gid = 'stop_point_gid_example' # str | 
    includes = [openapi_client.VTApiPlaneraResaWebV4ModelsDepartureDetailsIncludeType()] # List[VTApiPlaneraResaWebV4ModelsDepartureDetailsIncludeType] | The additional information to include in the response. (optional)

    try:
        # Returns details about a departure.
        api_response = api_instance.stop_points_stop_point_gid_departures_details_reference_details_get(details_reference, stop_point_gid, includes=includes)
        print("The response of StopPointsApi->stop_points_stop_point_gid_departures_details_reference_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StopPointsApi->stop_points_stop_point_gid_departures_details_reference_details_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details_reference** | **str**| The reference to the service journey, received from the departures call. A detailsReference is only valid during the same day as it was generated. | 
 **stop_point_gid** | **str**|  | 
 **includes** | [**List[VTApiPlaneraResaWebV4ModelsDepartureDetailsIncludeType]**](VTApiPlaneraResaWebV4ModelsDepartureDetailsIncludeType.md)| The additional information to include in the response. | [optional] 

### Return type

[**VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureDetailsApiModel**](VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureDetailsApiModel.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If service journey details were successfully retrieved. |  -  |
**400** | If any of the search parameters were invalid.&lt;br /&gt;              The following error codes can be returned:              1002: Missing details reference              1004: Corrupt details reference              5001: Bad service request              5003: Service error              6003: Faulty input |  -  |
**404** | If the details about the departure could not be found. |  -  |
**500** | If an internal server error occurred. |  -  |
**503** | If the service is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_points_stop_point_gid_departures_get**
> VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetDeparturesResponse stop_points_stop_point_gid_departures_get(stop_point_gid, start_date_time=start_date_time, time_span_in_minutes=time_span_in_minutes, max_departures_per_line_and_direction=max_departures_per_line_and_direction, limit=limit, offset=offset, include_occupancy=include_occupancy, direction_gid=direction_gid)

Returns departures from the specified stop point at the specified time.

Sample request:        GET /stop-points/9022014001760003/departures

### Example

* OAuth Authentication (auth):
```python
import time
import os
import openapi_client
from openapi_client.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_get_departures_response import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetDeparturesResponse
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
    api_instance = openapi_client.StopPointsApi(api_client)
    stop_point_gid = 'stop_point_gid_example' # str | The 16-digit Västtrafik gid of the stop point.
    start_date_time = 'start_date_time_example' # str | The start of the time interval for which to get upcoming departures. Must be specified in RFC 3339 format or be null which means that the current time on the server is used. (optional)
    time_span_in_minutes = 60 # int | The number of minutes from the start time for which to get upcoming departures. Allowed values are between 0 and 1440. (optional) (default to 60)
    max_departures_per_line_and_direction = 2 # int | The maximum number of departures for a single line in a specific direction. (optional) (default to 2)
    limit = 10 # int | The number of results to return. (optional) (default to 10)
    offset = 0 # int | The zero-based start offset of the pagination. (optional) (default to 0)
    include_occupancy = False # bool | Includes occupancy in departure. (optional) (default to False)
    direction_gid = 'direction_gid_example' # str | Filter result by last stop on journey. Must be a 16-digit Västtrafik stop area (optional)

    try:
        # Returns departures from the specified stop point at the specified time.
        api_response = api_instance.stop_points_stop_point_gid_departures_get(stop_point_gid, start_date_time=start_date_time, time_span_in_minutes=time_span_in_minutes, max_departures_per_line_and_direction=max_departures_per_line_and_direction, limit=limit, offset=offset, include_occupancy=include_occupancy, direction_gid=direction_gid)
        print("The response of StopPointsApi->stop_points_stop_point_gid_departures_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StopPointsApi->stop_points_stop_point_gid_departures_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stop_point_gid** | **str**| The 16-digit Västtrafik gid of the stop point. | 
 **start_date_time** | **str**| The start of the time interval for which to get upcoming departures. Must be specified in RFC 3339 format or be null which means that the current time on the server is used. | [optional] 
 **time_span_in_minutes** | **int**| The number of minutes from the start time for which to get upcoming departures. Allowed values are between 0 and 1440. | [optional] [default to 60]
 **max_departures_per_line_and_direction** | **int**| The maximum number of departures for a single line in a specific direction. | [optional] [default to 2]
 **limit** | **int**| The number of results to return. | [optional] [default to 10]
 **offset** | **int**| The zero-based start offset of the pagination. | [optional] [default to 0]
 **include_occupancy** | **bool**| Includes occupancy in departure. | [optional] [default to False]
 **direction_gid** | **str**| Filter result by last stop on journey. Must be a 16-digit Västtrafik stop area | [optional] 

### Return type

[**VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetDeparturesResponse**](VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetDeparturesResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If departures were successfully retrieved. |  -  |
**400** | If the search text, any of the specified types or the pagination properties are invalid.&lt;br /&gt;              The following error codes can be returned:              4101: Invalid limit and offset values              4103: Invalid start datetime              4104: Invalid timespan              4105: Invalid max departures per line and direction              4107: Invalid stop point gid              4108: Invalid direction gid              5001: Bad service request |  -  |
**404** | If the stop point was not found. |  -  |
**500** | If an internal server error occurred. |  -  |
**503** | If the service is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

