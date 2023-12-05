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

from openapi_client.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_arrival_details_api_model import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel  # noqa: E501

class TestVTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel(unittest.TestCase):
    """VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel:
        """Test VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel`
        """
        model = VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel()  # noqa: E501
        if include_optional:
            return VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel(
                service_journeys = [
                    openapi_client.models.vt/api_planera_resa/web/v4/models/departures_and_arrivals/service_journey_details_api_model.VT.ApiPlaneraResa.Web.V4.Models.DeparturesAndArrivals.ServiceJourneyDetailsApiModel(
                        gid = '', 
                        direction = '', 
                        line = openapi_client.models.vt/api_planera_resa/web/v4/models/departures_and_arrivals/line_details_api_model.VT.ApiPlaneraResa.Web.V4.Models.DeparturesAndArrivals.LineDetailsApiModel(
                            name = '', 
                            background_color = '', 
                            foreground_color = '', 
                            border_color = '', 
                            transport_mode = 'unknown', 
                            transport_sub_mode = 'unknown', ), 
                        service_journey_coordinates = [
                            openapi_client.models.vt/api_planera_resa/web/v4/models/departures_and_arrivals/coordinate_api_model.VT.ApiPlaneraResa.Web.V4.Models.DeparturesAndArrivals.CoordinateApiModel(
                                latitude = 1.337, 
                                longitude = 1.337, 
                                elevation = 1.337, )
                            ], 
                        calls_on_service_journey = [
                            openapi_client.models.vt/api_planera_resa/web/v4/models/departures_and_arrivals/call_details_api_model.VT.ApiPlaneraResa.Web.V4.Models.DeparturesAndArrivals.CallDetailsApiModel(
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
                                planned_arrival_time = '', 
                                planned_departure_time = '', 
                                estimated_arrival_time = '', 
                                estimated_departure_time = '', 
                                estimated_otherwise_planned_arrival_time = '', 
                                estimated_otherwise_planned_departure_time = '', 
                                planned_platform = '', 
                                estimated_platform = '', 
                                latitude = 1.337, 
                                longitude = 1.337, 
                                index = '', 
                                occupancy = openapi_client.models.vt/api_planera_resa/web/v4/models/occupancy_information_api_model.VT.ApiPlaneraResa.Web.V4.Models.OccupancyInformationApiModel(
                                    level = 'low', 
                                    source = 'prediction', ), 
                                is_cancelled = True, 
                                is_departure_cancelled = True, 
                                is_arrival_cancelled = True, )
                            ], )
                    ]
            )
        else:
            return VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel(
        )
        """

    def testVTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel(self):
        """Test VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
