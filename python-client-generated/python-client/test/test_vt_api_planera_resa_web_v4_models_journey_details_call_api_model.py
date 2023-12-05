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

from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_call_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsCallApiModel  # noqa: E501

class TestVTApiPlaneraResaWebV4ModelsJourneyDetailsCallApiModel(unittest.TestCase):
    """VTApiPlaneraResaWebV4ModelsJourneyDetailsCallApiModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VTApiPlaneraResaWebV4ModelsJourneyDetailsCallApiModel:
        """Test VTApiPlaneraResaWebV4ModelsJourneyDetailsCallApiModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VTApiPlaneraResaWebV4ModelsJourneyDetailsCallApiModel`
        """
        model = VTApiPlaneraResaWebV4ModelsJourneyDetailsCallApiModel()  # noqa: E501
        if include_optional:
            return VTApiPlaneraResaWebV4ModelsJourneyDetailsCallApiModel(
                stop_point = openapi_client.models.vt/api_planera_resa/web/v4/models/journey_details/stop_point_api_model.VT.ApiPlaneraResa.Web.V4.Models.JourneyDetails.StopPointApiModel(
                    gid = '0', 
                    name = '0', 
                    platform = '', 
                    latitude = 1.337, 
                    longitude = 1.337, 
                    stop_area = openapi_client.models.vt/api_planera_resa/web/v4/models/journey_details/stop_area_api_model.VT.ApiPlaneraResa.Web.V4.Models.JourneyDetails.StopAreaApiModel(
                        gid = '', 
                        name = '', 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        tariff_zone1 = openapi_client.models.vt/api_planera_resa/web/v4/models/journey_details/tariff_zone_api_model.VT.ApiPlaneraResa.Web.V4.Models.JourneyDetails.TariffZoneApiModel(
                            gid = '', 
                            name = '', 
                            number = 56, 
                            short_name = '', ), 
                        tariff_zone2 = openapi_client.models.vt/api_planera_resa/web/v4/models/journey_details/tariff_zone_api_model.VT.ApiPlaneraResa.Web.V4.Models.JourneyDetails.TariffZoneApiModel(
                            gid = '', 
                            name = '', 
                            number = 56, 
                            short_name = '', ), ), ),
                planned_time = '0',
                estimated_time = '',
                estimated_otherwise_planned_time = '',
                notes = [
                    openapi_client.models.vt/api_planera_resa/core/models/note.VT.ApiPlaneraResa.Core.Models.Note(
                        type = '', 
                        severity = 'unknown', 
                        text = '', )
                    ]
            )
        else:
            return VTApiPlaneraResaWebV4ModelsJourneyDetailsCallApiModel(
                stop_point = openapi_client.models.vt/api_planera_resa/web/v4/models/journey_details/stop_point_api_model.VT.ApiPlaneraResa.Web.V4.Models.JourneyDetails.StopPointApiModel(
                    gid = '0', 
                    name = '0', 
                    platform = '', 
                    latitude = 1.337, 
                    longitude = 1.337, 
                    stop_area = openapi_client.models.vt/api_planera_resa/web/v4/models/journey_details/stop_area_api_model.VT.ApiPlaneraResa.Web.V4.Models.JourneyDetails.StopAreaApiModel(
                        gid = '', 
                        name = '', 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        tariff_zone1 = openapi_client.models.vt/api_planera_resa/web/v4/models/journey_details/tariff_zone_api_model.VT.ApiPlaneraResa.Web.V4.Models.JourneyDetails.TariffZoneApiModel(
                            gid = '', 
                            name = '', 
                            number = 56, 
                            short_name = '', ), 
                        tariff_zone2 = openapi_client.models.vt/api_planera_resa/web/v4/models/journey_details/tariff_zone_api_model.VT.ApiPlaneraResa.Web.V4.Models.JourneyDetails.TariffZoneApiModel(
                            gid = '', 
                            name = '', 
                            number = 56, 
                            short_name = '', ), ), ),
                planned_time = '0',
        )
        """

    def testVTApiPlaneraResaWebV4ModelsJourneyDetailsCallApiModel(self):
        """Test VTApiPlaneraResaWebV4ModelsJourneyDetailsCallApiModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
