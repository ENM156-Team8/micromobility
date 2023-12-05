# openapi_client.JourneysApi

All URIs are relative to *https://ext-api.vasttrafik.se/pr/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**journeys_details_reference_details_get**](JourneysApi.md#journeys_details_reference_details_get) | **GET** /journeys/{detailsReference}/details | Returns details about a journey.
[**journeys_get**](JourneysApi.md#journeys_get) | **GET** /journeys | Returns journeys matching the specified search parameters.
[**journeys_reconstruct_get**](JourneysApi.md#journeys_reconstruct_get) | **GET** /journeys/reconstruct | Reconstructs a journey based on the given reconstruction reference, received from the search journeys query.
[**journeys_valid_time_interval_get**](JourneysApi.md#journeys_valid_time_interval_get) | **GET** /journeys/valid-time-interval | Returns a time interval for when journey data is available.


# **journeys_details_reference_details_get**
> VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel journeys_details_reference_details_get(details_reference, includes=includes, channel_ids=channel_ids, product_types=product_types, traveller_categories=traveller_categories)

Returns details about a journey.

Sample request:        GET /journeys/{detailsReference}/details?includes=ticketsuggestions

### Example

* OAuth Authentication (auth):
```python
import time
import os
import openapi_client
from openapi_client.models.vt_api_planera_resa_core_models_traveller_category import VTApiPlaneraResaCoreModelsTravellerCategory
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_include_type import VTApiPlaneraResaWebV4ModelsJourneyDetailsIncludeType
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_journey_details_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel
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
    api_instance = openapi_client.JourneysApi(api_client)
    details_reference = 'details_reference_example' # str | The reference to the journey, received from the search journeys query. A detailsReference is only valid during the same day as it was generated.
    includes = [openapi_client.VTApiPlaneraResaWebV4ModelsJourneyDetailsIncludeType()] # List[VTApiPlaneraResaWebV4ModelsJourneyDetailsIncludeType] | The additional information to include in the response. (optional)
    channel_ids = [56] # List[int] | List of channel ids to include if 'ticketsuggestions' is set in the 'includes' parameter. Optional parameter. (optional)
    product_types = [56] # List[int] | List of product type ids to include if 'ticketsuggestions' is set in the 'includes' parameter. Optional parameter. (optional)
    traveller_categories = [openapi_client.VTApiPlaneraResaCoreModelsTravellerCategory()] # List[VTApiPlaneraResaCoreModelsTravellerCategory] | List of traveller category ids to include if 'ticketsuggestions' is set in the 'includes' parameter. Optional parameter. (optional)

    try:
        # Returns details about a journey.
        api_response = api_instance.journeys_details_reference_details_get(details_reference, includes=includes, channel_ids=channel_ids, product_types=product_types, traveller_categories=traveller_categories)
        print("The response of JourneysApi->journeys_details_reference_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JourneysApi->journeys_details_reference_details_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details_reference** | **str**| The reference to the journey, received from the search journeys query. A detailsReference is only valid during the same day as it was generated. | 
 **includes** | [**List[VTApiPlaneraResaWebV4ModelsJourneyDetailsIncludeType]**](VTApiPlaneraResaWebV4ModelsJourneyDetailsIncludeType.md)| The additional information to include in the response. | [optional] 
 **channel_ids** | [**List[int]**](int.md)| List of channel ids to include if &#39;ticketsuggestions&#39; is set in the &#39;includes&#39; parameter. Optional parameter. | [optional] 
 **product_types** | [**List[int]**](int.md)| List of product type ids to include if &#39;ticketsuggestions&#39; is set in the &#39;includes&#39; parameter. Optional parameter. | [optional] 
 **traveller_categories** | [**List[VTApiPlaneraResaCoreModelsTravellerCategory]**](VTApiPlaneraResaCoreModelsTravellerCategory.md)| List of traveller category ids to include if &#39;ticketsuggestions&#39; is set in the &#39;includes&#39; parameter. Optional parameter. | [optional] 

### Return type

[**VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel**](VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If journeys details were successfully retrieved. |  -  |
**400** | If any of the search parameters were invalid.&lt;br /&gt;              The following error codes can be returned:              1001: Ticket suggestion argument failed              1002: Missing details reference              1004: Corrupt details reference              5001: Bad service request              5003: Service error              6003: Faulty input              6007: Unsuccessful search              6009: Incomplete search |  -  |
**404** | If the specified journey could not be found. |  -  |
**500** | If an internal server error occurred. |  -  |
**503** | If the service is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journeys_get**
> VTApiPlaneraResaWebV4ModelsJourneysGetJourneysResponse journeys_get(origin_gid=origin_gid, origin_name=origin_name, origin_latitude=origin_latitude, origin_longitude=origin_longitude, destination_gid=destination_gid, destination_name=destination_name, destination_latitude=destination_latitude, destination_longitude=destination_longitude, date_time=date_time, date_time_relates_to=date_time_relates_to, pagination_reference=pagination_reference, limit=limit, transport_modes=transport_modes, transport_sub_modes=transport_sub_modes, only_direct_connections=only_direct_connections, include_nearby_stop_areas=include_nearby_stop_areas, via_gid=via_gid, origin_walk=origin_walk, dest_walk=dest_walk, origin_bike=origin_bike, dest_bike=dest_bike, total_bike=total_bike, origin_car=origin_car, dest_car=dest_car, origin_park=origin_park, dest_park=dest_park, interchange_duration_in_minutes=interchange_duration_in_minutes, include_occupancy=include_occupancy)

Returns journeys matching the specified search parameters.

For an origin or destination to be valid, either a gid or a combination of latitude and longitude must be specified. OriginName and destinationName are optional in combination with latitude and longitude.    Sample request:        GET /journeys?originGid=9021014001760000&destinationGid=9021014003980000    or        GET /journeys?originName=Sadelsten,+V%C3%A5rg%C3%A5rda&originLongitude=12.63308&originLatitude=58.028237&destinationLongitude=11.930897&destinationLatitude=57.586085&destinationName=%C3%85sdammsstigen,+427+36+Billdal

### Example

* OAuth Authentication (auth):
```python
import time
import os
import openapi_client
from openapi_client.models.vt_api_planera_resa_core_models_date_time_relates_to_type import VTApiPlaneraResaCoreModelsDateTimeRelatesToType
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_transport_mode import VTApiPlaneraResaWebV4ModelsJourneyTransportMode
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_transport_sub_mode import VTApiPlaneraResaWebV4ModelsJourneyTransportSubMode
from openapi_client.models.vt_api_planera_resa_web_v4_models_journeys_get_journeys_response import VTApiPlaneraResaWebV4ModelsJourneysGetJourneysResponse
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
    api_instance = openapi_client.JourneysApi(api_client)
    origin_gid = 'origin_gid_example' # str | The 16-digit Västtrafik gid of the origin location (which could be either a stop area (e.g. '9021014001760000'), a stop point (e.g. '9022014001760004') or meta-station (e.g. '0000000800000022')). (optional)
    origin_name = 'origin_name_example' # str | The name of the origin location. The maximum length allowed is 256 characters. (optional)
    origin_latitude = 3.4 # float | The latitude of the origin location. (optional)
    origin_longitude = 3.4 # float | The longitude of the origin location. (optional)
    destination_gid = 'destination_gid_example' # str | The 16-digit Västtrafik gid of the destination location (which could be either a stop area, stop point or meta-station). (optional)
    destination_name = 'destination_name_example' # str | The name of the destination location. The maximum length allowed is 256 characters. (optional)
    destination_latitude = 3.4 # float | The latitude of the destination location. (optional)
    destination_longitude = 3.4 # float | The longitude of the destination location. (optional)
    date_time = '2013-10-20T19:20:30+01:00' # datetime | The datetime for which to search journeys. Must be specified in RFC 3339 format or be null which means that the current time on the server is used. The related dateTimeRelatesTo parameter specifies if the time is related to the arrival or departure. (optional)
    date_time_relates_to = openapi_client.VTApiPlaneraResaCoreModelsDateTimeRelatesToType() # VTApiPlaneraResaCoreModelsDateTimeRelatesToType | Specifies if the datetime is related to the departure or arrival of the journey. (optional)
    pagination_reference = 'pagination_reference_example' # str | Pagination reference from a previous search. (optional)
    limit = 10 # int | The number of results to return. Not guaranteed to return the specified number of results and usually not more than 7 results. (optional) (default to 10)
    transport_modes = [openapi_client.VTApiPlaneraResaWebV4ModelsJourneyTransportMode()] # List[VTApiPlaneraResaWebV4ModelsJourneyTransportMode] | The transport modes to include when searching for journeys, if none specified all transport modes are included. (optional)
    transport_sub_modes = [openapi_client.VTApiPlaneraResaWebV4ModelsJourneyTransportSubMode()] # List[VTApiPlaneraResaWebV4ModelsJourneyTransportSubMode] | The transport sub modes to include when searching for journeys, if none specified all transport sub modes are included. Only supported in combination with transportMode 'train'. (optional)
    only_direct_connections = False # bool | Only include direct connections, e.g. journeys with one trip leg. (optional) (default to False)
    include_nearby_stop_areas = False # bool | Includes nearby stop areas when searching for a journey to or from a stop area or stop point. This means that the search algorithm will take additional stop points of other stop areas nearby the given start and destination stop area into account. These additional stop points are reachable by walk. E.g when true a journey suggestion may include a departure access link (initial walking leg) to a stop point of a stop area close by the specified origin stop area. (optional) (default to False)
    via_gid = 56 # int | The 16-digit Västtrafik gid of the via location (which must be a stop area). (optional)
    origin_walk = 'origin_walk_example' # str | Enables/disables using footpaths in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable walk with a minimum distance of 0 meters and a maximum distance of 3 kilometers, set the parameter originWalk=1,0,3000. If default distances should be used, skip the values, e.g 1,,. This will enable walk with the default minimum (0 meters) and the default maximum (2000 meters). (optional)
    dest_walk = 'dest_walk_example' # str | Enables/disables using footpaths at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable walk with a minimum distance of 0 meters and a maximum distance of 3 kilometers, set the parameter destWalk=1,0,3000. If default distances should be used, skip the values, e.g 1,,. This will enable walk with the default minimum (0 meters) and the default maximum (2000 meters). (optional)
    origin_bike = 'origin_bike_example' # str | Enables/disables using bike paths in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable bike with a minimum distance of 1000 meters and a maximum distance of 5 kilometers, set the parameter originBike=1,1000,5000. If default distances should be used, skip the values, e.g 1,,. This will enable bike with the default minimum (0 meters) and the default maximum (3000 meters). (optional)
    dest_bike = 'dest_bike_example' # str | Enables/disables using bike paths at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable bike with a minimum distance of 1000 meters and a maximum distance of 5 kilometers, set the parameter destBike=1,1000,5000. If default distances should be used, skip the values, e.g 1,,. This will enable bike with the default minimum (0 meters) and the default maximum (3000 meters). (optional)
    total_bike = 'total_bike_example' # str | Enables/disables using bike routes for the whole trip. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable bike with a minimum distance of 0 meters and a maximum distance of 20 kilometers, set the parameter totalBike=1,0,20000. If default distances should be used, skip the values, e.g 1,,. This will enable bike with the default minimum (0 meters) and the default maximum (25000 meters). (optional)
    origin_car = 'origin_car_example' # str | Enables/disables using car in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable car with a minimum distance of 2000 meters and a maximum distance of 7 kilometers, set the parameter origincar=1,2000,7000. If default distances should be used, skip the values, e.g 1,,. This will enable car with the default minimum (0 meters) and the default maximum (5000 meters). (optional)
    dest_car = 'dest_car_example' # str | Enables/disables using car at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable car with a minimum distance of 2000 meters and a maximum distance of 7 kilometers, set the parameter destCar=1,2000,7000. If default distances should be used, skip the values, e.g 1,,. This will enable car with the default minimum (0 meters) and the default maximum (5000 meters). (optional)
    origin_park = 'origin_park_example' # str | Enables/disables using Park and Ride in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable Park and Ride with a minimum distance of 3000 meters and a maximum distance of 70 kilometers, set the parameter originPark=1,3000,70000. If default distances should be used, skip the values, e.g 1,,. This will enable Park and Ride with the default minimum (2000 meters) and the default maximum (50000 meters). (optional)
    dest_park = 'dest_park_example' # str | Enables/disables using Park and Ride at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable Park and Ride with a minimum distance of 3000 meters and a maximum distance of 70 kilometers, set the parameter destPark=1,3000,70000. If default distances should be used, skip the values, e.g 1,,. This will enable Park and Ride with the default minimum (2000 meters) and the default maximum (50000 meters). (optional)
    interchange_duration_in_minutes = 56 # int | The minimum number of minutes between arrival and departure for a connection to be valid and the trip included in the search results, ignoring the default value. (optional)
    include_occupancy = False # bool | Includes occupancy in journey. (optional) (default to False)

    try:
        # Returns journeys matching the specified search parameters.
        api_response = api_instance.journeys_get(origin_gid=origin_gid, origin_name=origin_name, origin_latitude=origin_latitude, origin_longitude=origin_longitude, destination_gid=destination_gid, destination_name=destination_name, destination_latitude=destination_latitude, destination_longitude=destination_longitude, date_time=date_time, date_time_relates_to=date_time_relates_to, pagination_reference=pagination_reference, limit=limit, transport_modes=transport_modes, transport_sub_modes=transport_sub_modes, only_direct_connections=only_direct_connections, include_nearby_stop_areas=include_nearby_stop_areas, via_gid=via_gid, origin_walk=origin_walk, dest_walk=dest_walk, origin_bike=origin_bike, dest_bike=dest_bike, total_bike=total_bike, origin_car=origin_car, dest_car=dest_car, origin_park=origin_park, dest_park=dest_park, interchange_duration_in_minutes=interchange_duration_in_minutes, include_occupancy=include_occupancy)
        print("The response of JourneysApi->journeys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JourneysApi->journeys_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin_gid** | **str**| The 16-digit Västtrafik gid of the origin location (which could be either a stop area (e.g. &#39;9021014001760000&#39;), a stop point (e.g. &#39;9022014001760004&#39;) or meta-station (e.g. &#39;0000000800000022&#39;)). | [optional] 
 **origin_name** | **str**| The name of the origin location. The maximum length allowed is 256 characters. | [optional] 
 **origin_latitude** | **float**| The latitude of the origin location. | [optional] 
 **origin_longitude** | **float**| The longitude of the origin location. | [optional] 
 **destination_gid** | **str**| The 16-digit Västtrafik gid of the destination location (which could be either a stop area, stop point or meta-station). | [optional] 
 **destination_name** | **str**| The name of the destination location. The maximum length allowed is 256 characters. | [optional] 
 **destination_latitude** | **float**| The latitude of the destination location. | [optional] 
 **destination_longitude** | **float**| The longitude of the destination location. | [optional] 
 **date_time** | **datetime**| The datetime for which to search journeys. Must be specified in RFC 3339 format or be null which means that the current time on the server is used. The related dateTimeRelatesTo parameter specifies if the time is related to the arrival or departure. | [optional] 
 **date_time_relates_to** | [**VTApiPlaneraResaCoreModelsDateTimeRelatesToType**](.md)| Specifies if the datetime is related to the departure or arrival of the journey. | [optional] 
 **pagination_reference** | **str**| Pagination reference from a previous search. | [optional] 
 **limit** | **int**| The number of results to return. Not guaranteed to return the specified number of results and usually not more than 7 results. | [optional] [default to 10]
 **transport_modes** | [**List[VTApiPlaneraResaWebV4ModelsJourneyTransportMode]**](VTApiPlaneraResaWebV4ModelsJourneyTransportMode.md)| The transport modes to include when searching for journeys, if none specified all transport modes are included. | [optional] 
 **transport_sub_modes** | [**List[VTApiPlaneraResaWebV4ModelsJourneyTransportSubMode]**](VTApiPlaneraResaWebV4ModelsJourneyTransportSubMode.md)| The transport sub modes to include when searching for journeys, if none specified all transport sub modes are included. Only supported in combination with transportMode &#39;train&#39;. | [optional] 
 **only_direct_connections** | **bool**| Only include direct connections, e.g. journeys with one trip leg. | [optional] [default to False]
 **include_nearby_stop_areas** | **bool**| Includes nearby stop areas when searching for a journey to or from a stop area or stop point. This means that the search algorithm will take additional stop points of other stop areas nearby the given start and destination stop area into account. These additional stop points are reachable by walk. E.g when true a journey suggestion may include a departure access link (initial walking leg) to a stop point of a stop area close by the specified origin stop area. | [optional] [default to False]
 **via_gid** | **int**| The 16-digit Västtrafik gid of the via location (which must be a stop area). | [optional] 
 **origin_walk** | **str**| Enables/disables using footpaths in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable walk with a minimum distance of 0 meters and a maximum distance of 3 kilometers, set the parameter originWalk&#x3D;1,0,3000. If default distances should be used, skip the values, e.g 1,,. This will enable walk with the default minimum (0 meters) and the default maximum (2000 meters). | [optional] 
 **dest_walk** | **str**| Enables/disables using footpaths at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable walk with a minimum distance of 0 meters and a maximum distance of 3 kilometers, set the parameter destWalk&#x3D;1,0,3000. If default distances should be used, skip the values, e.g 1,,. This will enable walk with the default minimum (0 meters) and the default maximum (2000 meters). | [optional] 
 **origin_bike** | **str**| Enables/disables using bike paths in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable bike with a minimum distance of 1000 meters and a maximum distance of 5 kilometers, set the parameter originBike&#x3D;1,1000,5000. If default distances should be used, skip the values, e.g 1,,. This will enable bike with the default minimum (0 meters) and the default maximum (3000 meters). | [optional] 
 **dest_bike** | **str**| Enables/disables using bike paths at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable bike with a minimum distance of 1000 meters and a maximum distance of 5 kilometers, set the parameter destBike&#x3D;1,1000,5000. If default distances should be used, skip the values, e.g 1,,. This will enable bike with the default minimum (0 meters) and the default maximum (3000 meters). | [optional] 
 **total_bike** | **str**| Enables/disables using bike routes for the whole trip. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable bike with a minimum distance of 0 meters and a maximum distance of 20 kilometers, set the parameter totalBike&#x3D;1,0,20000. If default distances should be used, skip the values, e.g 1,,. This will enable bike with the default minimum (0 meters) and the default maximum (25000 meters). | [optional] 
 **origin_car** | **str**| Enables/disables using car in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable car with a minimum distance of 2000 meters and a maximum distance of 7 kilometers, set the parameter origincar&#x3D;1,2000,7000. If default distances should be used, skip the values, e.g 1,,. This will enable car with the default minimum (0 meters) and the default maximum (5000 meters). | [optional] 
 **dest_car** | **str**| Enables/disables using car at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable car with a minimum distance of 2000 meters and a maximum distance of 7 kilometers, set the parameter destCar&#x3D;1,2000,7000. If default distances should be used, skip the values, e.g 1,,. This will enable car with the default minimum (0 meters) and the default maximum (5000 meters). | [optional] 
 **origin_park** | **str**| Enables/disables using Park and Ride in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable Park and Ride with a minimum distance of 3000 meters and a maximum distance of 70 kilometers, set the parameter originPark&#x3D;1,3000,70000. If default distances should be used, skip the values, e.g 1,,. This will enable Park and Ride with the default minimum (2000 meters) and the default maximum (50000 meters). | [optional] 
 **dest_park** | **str**| Enables/disables using Park and Ride at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable Park and Ride with a minimum distance of 3000 meters and a maximum distance of 70 kilometers, set the parameter destPark&#x3D;1,3000,70000. If default distances should be used, skip the values, e.g 1,,. This will enable Park and Ride with the default minimum (2000 meters) and the default maximum (50000 meters). | [optional] 
 **interchange_duration_in_minutes** | **int**| The minimum number of minutes between arrival and departure for a connection to be valid and the trip included in the search results, ignoring the default value. | [optional] 
 **include_occupancy** | **bool**| Includes occupancy in journey. | [optional] [default to False]

### Return type

[**VTApiPlaneraResaWebV4ModelsJourneysGetJourneysResponse**](VTApiPlaneraResaWebV4ModelsJourneysGetJourneysResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the search was successfully completed. |  -  |
**400** | If any of the search parameters were invalid.&lt;br /&gt;              The following error codes can be returned:              2001: Limit must be greater than zero              2002: Invalid location              2003: Invalid datetime              2004: Decoding pagination reference failed              2005: Invalid transport mode to origin              2006: Transport sub modes without transport modes              2007: Invalid origin gid              2008: Invalid destination gid              2009: Invalid via gid              2010: Invalid interchange duration              2011: Invalid origin walk              2012: Invalid destination walk              2013: Invalid origin bike              2014: Invalid destination bike              2015: Invalid origin car              2016: Invalid destination car              2017: Invalid origin park              2018: Invalid destination park              2019: Invalid total bike              2020: Identical origin and destination              2021: Origin name exceeds maximum length              2022: Destination name exceeds maximum length              5001: Bad service request              5003: Service error              6001: Same origin and destination              6002: Error in date field              6003: Faulty input              6004: Unknown arrival station              6005: Unknown intermediate station              6006: Unknown departure station              6007: Unsuccessful search              6008: Nearby not found              6009: Incomplete search              6010: Origin/Destination are too near |  -  |
**500** | If an internal server error occurred. |  -  |
**503** | If the service is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journeys_reconstruct_get**
> VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel journeys_reconstruct_get(ref, include_occupancy=include_occupancy)

Reconstructs a journey based on the given reconstruction reference, received from the search journeys query.

Sample request:        GET /journeys/reconstruct?ref=¶HKI¶T$A=1@O=Brunnsparken, Göteborg@L=1760003@a=128@$A=1@O=Korsvägen, Göteborg@L=3980004@a=128@$202206131358$202206131406$Spå    4$$1$$$$$$¶KRCC¶#VE#1#

### Example

* OAuth Authentication (auth):
```python
import time
import os
import openapi_client
from openapi_client.models.vt_api_planera_resa_web_v4_models_journeys_journey_api_model import VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel
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
    api_instance = openapi_client.JourneysApi(api_client)
    ref = 'ref_example' # str | The reconstruction reference. A reconstructionReference is valid as long as the original journey search is valid.
    include_occupancy = False # bool | Includes occupancy in journey. (optional) (default to False)

    try:
        # Reconstructs a journey based on the given reconstruction reference, received from the search journeys query.
        api_response = api_instance.journeys_reconstruct_get(ref, include_occupancy=include_occupancy)
        print("The response of JourneysApi->journeys_reconstruct_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JourneysApi->journeys_reconstruct_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| The reconstruction reference. A reconstructionReference is valid as long as the original journey search is valid. | 
 **include_occupancy** | **bool**| Includes occupancy in journey. | [optional] [default to False]

### Return type

[**VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel**](VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the journey reconstruction was successful. |  -  |
**400** | If the reconstruction failed or if any of the parameters were invalid.&lt;br /&gt;              The following error codes can be returned:              1003: Missing reconstruction reference |  -  |
**500** | If an internal server error occurred. |  -  |
**503** | If the service is temporarily unavailable |  -  |
**404** | If the journey was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journeys_valid_time_interval_get**
> VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel journeys_valid_time_interval_get()

Returns a time interval for when journey data is available.

### Example

* OAuth Authentication (auth):
```python
import time
import os
import openapi_client
from openapi_client.models.vt_api_planera_resa_web_v4_models_valid_time_interval_api_model import VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel
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
    api_instance = openapi_client.JourneysApi(api_client)

    try:
        # Returns a time interval for when journey data is available.
        api_response = api_instance.journeys_valid_time_interval_get()
        print("The response of JourneysApi->journeys_valid_time_interval_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JourneysApi->journeys_valid_time_interval_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel**](VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If date range was successfully retrieved. |  -  |
**404** | If no time range could be found. |  -  |
**500** | If an internal server error occurred. |  -  |
**503** | If the service is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

