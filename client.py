import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
import generateAccess 
import apiHandler

# Defining the host is optional and defaults to https://ext-api.vasttrafik.se/pr/v4
# See configuration.py for a list of all supported configuration parameters.

configuration = openapi_client.Configuration(
    host="https://ext-api.vasttrafik.se/pr/v4",  
    api_key={
        'api_key_header': apiHandler.accessTokenVt
    },
    verify_ssl=True
)

with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_journey_instance = openapi_client.JourneysApi(api_client)
    origin_gid = '9021014001760000'
    destination_gid = '9021014003980000'
    try:
        #Returns details about a journey.
        api_response = api_journey_instance.journeys_get(origin_gid=origin_gid, destination_gid=destination_gid)
        print("The response of JourneysApi->journeys_details_reference_details_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JourneysApi->journeys_details_reference_details_get: %s\n" % e)