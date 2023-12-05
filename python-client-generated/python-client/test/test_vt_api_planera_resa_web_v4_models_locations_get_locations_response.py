# coding: utf-8

"""
    Planera Resa

    Sök och planera resor med Västtrafik

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.vt_api_planera_resa_web_v4_models_locations_get_locations_response import VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse  # noqa: E501

class TestVTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse(unittest.TestCase):
    """VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse:
        """Test VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse`
        """
        model = VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse()  # noqa: E501
        if include_optional:
            return VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse(
                results = [
                    openapi_client.models.vt/api_planera_resa/web/v4/models/locations/location_api_model.VT.ApiPlaneraResa.Web.V4.Models.Locations.LocationApiModel(
                        gid = '', 
                        name = '0', 
                        location_type = 'unknown', 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        platform = '', 
                        straight_line_distance_in_meters = 56, 
                        has_local_service = True, )
                    ],
                pagination = openapi_client.models.vt/api_planera_resa/web/v4/models/pagination_properties.VT.ApiPlaneraResa.Web.V4.Models.PaginationProperties(
                    limit = 56, 
                    offset = 56, 
                    size = 56, ),
                links = openapi_client.models.vt/api_planera_resa/web/v4/models/pagination_links.VT.ApiPlaneraResa.Web.V4.Models.PaginationLinks(
                    previous = '', 
                    next = '', 
                    current = '', )
            )
        else:
            return VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse(
        )
        """

    def testVTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse(self):
        """Test VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
