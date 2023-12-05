# openapi_client.LocationsApi

All URIs are relative to *https://ext-api.vasttrafik.se/pr/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_by_coordinates_get**](LocationsApi.md#locations_by_coordinates_get) | **GET** /locations/by-coordinates | Returns the locations nearest the specified coordinates. Currently only stop areas, stop points and meta-stations are supported.
[**locations_by_text_get**](LocationsApi.md#locations_by_text_get) | **GET** /locations/by-text | Returns locations matching the specified text. Currently only stop areas, addresses, points of interest and meta-stations are supported.


# **locations_by_coordinates_get**
> VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse locations_by_coordinates_get(latitude, longitude, radius_in_meters=radius_in_meters, types=types, limit=limit, offset=offset)

Returns the locations nearest the specified coordinates. Currently only stop areas, stop points and meta-stations are supported.

Sample request:        GET /locations/by-coordinates?latitude=57.708734&longitude=11.974764&radiusInMeters=500&limit=10&offset=0

### Example

* OAuth Authentication (auth):
```python
import time
import os
import openapi_client
from openapi_client.models.vt_api_planera_resa_web_v4_models_location_by_coordinates_type import VTApiPlaneraResaWebV4ModelsLocationByCoordinatesType
from openapi_client.models.vt_api_planera_resa_web_v4_models_locations_get_locations_response import VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse
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
    api_instance = openapi_client.LocationsApi(api_client)
    latitude = 3.4 # float | The latitude.
    longitude = 3.4 # float | The longitude.
    radius_in_meters = 500 # int | The search radius from the coordinates specified in meters. Must be a positive integer > 0. (optional) (default to 500)
    types = [openapi_client.VTApiPlaneraResaWebV4ModelsLocationByCoordinatesType()] # List[VTApiPlaneraResaWebV4ModelsLocationByCoordinatesType] | The location types to include in the response, if none specified all locations types are included. (optional)
    limit = 10 # int | The number of results to return. (optional) (default to 10)
    offset = 0 # int | The zero-based start offset of the pagination. (optional) (default to 0)

    try:
        # Returns the locations nearest the specified coordinates. Currently only stop areas, stop points and meta-stations are supported.
        api_response = api_instance.locations_by_coordinates_get(latitude, longitude, radius_in_meters=radius_in_meters, types=types, limit=limit, offset=offset)
        print("The response of LocationsApi->locations_by_coordinates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->locations_by_coordinates_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **float**| The latitude. | 
 **longitude** | **float**| The longitude. | 
 **radius_in_meters** | **int**| The search radius from the coordinates specified in meters. Must be a positive integer &gt; 0. | [optional] [default to 500]
 **types** | [**List[VTApiPlaneraResaWebV4ModelsLocationByCoordinatesType]**](VTApiPlaneraResaWebV4ModelsLocationByCoordinatesType.md)| The location types to include in the response, if none specified all locations types are included. | [optional] 
 **limit** | **int**| The number of results to return. | [optional] [default to 10]
 **offset** | **int**| The zero-based start offset of the pagination. | [optional] [default to 0]

### Return type

[**VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse**](VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the search was successfully completed. |  -  |
**400** | If the coordinates, any of the specified types or the pagination properties are invalid.&lt;br /&gt;              The following error codes can be returned:              4001: Invalid limit and offset values              4002: Missing coordinates              4003: Invalid radius              5001: Bad service request |  -  |
**500** | If an internal server error occurred. |  -  |
**503** | If the service is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_by_text_get**
> VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse locations_by_text_get(q, types=types, limit=limit, offset=offset)

Returns locations matching the specified text. Currently only stop areas, addresses, points of interest and meta-stations are supported.

Sample request:        GET /locations/by-text?q=brunnsparken&limit=10&offset=0

### Example

* OAuth Authentication (auth):
```python
import time
import os
import openapi_client
from openapi_client.models.vt_api_planera_resa_web_v4_models_location_by_text_type import VTApiPlaneraResaWebV4ModelsLocationByTextType
from openapi_client.models.vt_api_planera_resa_web_v4_models_locations_get_locations_response import VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse
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
    api_instance = openapi_client.LocationsApi(api_client)
    q = 'q_example' # str | The search text (e.g. 'brunn', 'cent' or 'Kungsgatan'). The maximum length allowed is 256 characters.
    types = [openapi_client.VTApiPlaneraResaWebV4ModelsLocationByTextType()] # List[VTApiPlaneraResaWebV4ModelsLocationByTextType] | The location types to include in the response, if none specified all locations types are included. (optional)
    limit = 10 # int | The number of results to return. (optional) (default to 10)
    offset = 0 # int | The zero-based start offset of the pagination. (optional) (default to 0)

    try:
        # Returns locations matching the specified text. Currently only stop areas, addresses, points of interest and meta-stations are supported.
        api_response = api_instance.locations_by_text_get(q, types=types, limit=limit, offset=offset)
        print("The response of LocationsApi->locations_by_text_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->locations_by_text_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The search text (e.g. &#39;brunn&#39;, &#39;cent&#39; or &#39;Kungsgatan&#39;). The maximum length allowed is 256 characters. | 
 **types** | [**List[VTApiPlaneraResaWebV4ModelsLocationByTextType]**](VTApiPlaneraResaWebV4ModelsLocationByTextType.md)| The location types to include in the response, if none specified all locations types are included. | [optional] 
 **limit** | **int**| The number of results to return. | [optional] [default to 10]
 **offset** | **int**| The zero-based start offset of the pagination. | [optional] [default to 0]

### Return type

[**VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse**](VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the search was successfully completed. |  -  |
**400** | If the search text, any of the specified types or the pagination properties are invalid.&lt;br /&gt;              The following error codes can be returned:              3001: Missing query parameter              3002: Invalid limit and offset values              3003: Query parameter exceeds maximum length              5001: Bad service request |  -  |
**500** | If an internal server error occurred. |  -  |
**503** | If the service is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

