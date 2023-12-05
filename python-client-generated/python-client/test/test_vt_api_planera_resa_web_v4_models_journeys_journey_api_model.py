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

from openapi_client.models.vt_api_planera_resa_web_v4_models_journeys_journey_api_model import VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel  # noqa: E501

class TestVTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel(unittest.TestCase):
    """VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel:
        """Test VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel`
        """
        model = VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel()  # noqa: E501
        if include_optional:
            return VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel(
                reconstruction_reference = '',
                details_reference = '',
                departure_access_link = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/departure_access_link_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.DepartureAccessLinkApiModel(
                    transport_mode = 'unknown', 
                    transport_sub_mode = 'unknown', 
                    origin = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/link_endpoint_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.LinkEndpointApiModel(
                        gid = '', 
                        name = '0', 
                        location_type = 'unknown', 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        planned_time = '0', 
                        estimated_time = '', 
                        estimated_otherwise_planned_time = '', 
                        notes = [
                            openapi_client.models.vt/api_planera_resa/core/models/note.VT.ApiPlaneraResa.Core.Models.Note(
                                type = '', 
                                severity = 'unknown', 
                                text = '', )
                            ], ), 
                    destination = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/call_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.CallApiModel(
                        stop_point = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/stop_point_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.StopPointApiModel(
                            gid = '0', 
                            name = '0', 
                            platform = '', 
                            latitude = 1.337, 
                            longitude = 1.337, 
                            stop_area = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/stop_area_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.StopAreaApiModel(
                                gid = '', 
                                name = '', 
                                latitude = 1.337, 
                                longitude = 1.337, 
                                tariff_zone1 = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/tariff_zone_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.TariffZoneApiModel(
                                    gid = '', 
                                    name = '', 
                                    number = 56, 
                                    short_name = '', ), 
                                tariff_zone2 = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/tariff_zone_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.TariffZoneApiModel(
                                    gid = '', 
                                    name = '', 
                                    number = 56, 
                                    short_name = '', ), ), ), 
                        planned_time = '0', 
                        estimated_time = '', 
                        estimated_otherwise_planned_time = '', ), 
                    notes = [
                        openapi_client.models.vt/api_planera_resa/core/models/note.VT.ApiPlaneraResa.Core.Models.Note(
                            type = '', 
                            text = '', )
                        ], 
                    distance_in_meters = 56, 
                    planned_departure_time = '', 
                    planned_arrival_time = '', 
                    planned_duration_in_minutes = 56, 
                    estimated_departure_time = '', 
                    estimated_arrival_time = '', 
                    estimated_duration_in_minutes = 56, 
                    estimated_number_of_steps = 56, 
                    link_coordinates = [
                        openapi_client.models.vt/api_planera_resa/web/v4/models/coordinate_api_model.VT.ApiPlaneraResa.Web.V4.Models.CoordinateApiModel(
                            latitude = 1.337, 
                            longitude = 1.337, 
                            elevation = 1.337, 
                            is_on_trip_leg = True, 
                            is_trip_leg_start = True, 
                            is_trip_leg_stop = True, )
                        ], 
                    segments = [
                        openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/link_segment_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.LinkSegmentApiModel(
                            name = '', 
                            maneuver = 'none', 
                            orientation = 'unknown', 
                            maneuver_description = '', 
                            distance_in_meters = 56, )
                        ], ),
                trip_legs = [
                    openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/trip_leg_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.TripLegApiModel(
                        origin = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/call_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.CallApiModel(
                            stop_point = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/stop_point_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.StopPointApiModel(
                                gid = '0', 
                                name = '0', 
                                platform = '', 
                                latitude = 1.337, 
                                longitude = 1.337, 
                                stop_area = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/stop_area_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.StopAreaApiModel(
                                    gid = '', 
                                    name = '', 
                                    latitude = 1.337, 
                                    longitude = 1.337, 
                                    tariff_zone1 = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/tariff_zone_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.TariffZoneApiModel(
                                        gid = '', 
                                        name = '', 
                                        number = 56, 
                                        short_name = '', ), 
                                    tariff_zone2 = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/tariff_zone_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.TariffZoneApiModel(
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
                                ], ), 
                        destination = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/call_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.CallApiModel(
                            stop_point = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/stop_point_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.StopPointApiModel(
                                gid = '0', 
                                name = '0', 
                                platform = '', 
                                latitude = 1.337, 
                                longitude = 1.337, ), 
                            planned_time = '0', 
                            estimated_time = '', 
                            estimated_otherwise_planned_time = '', ), 
                        is_cancelled = True, 
                        is_part_cancelled = True, 
                        service_journey = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/service_journey_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.ServiceJourneyApiModel(
                            gid = '0', 
                            direction = '', 
                            number = '', 
                            line = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/line_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.LineApiModel(
                                name = '', 
                                background_color = '', 
                                foreground_color = '', 
                                border_color = '', 
                                transport_mode = 'unknown', 
                                transport_sub_mode = 'unknown', 
                                short_name = '', 
                                designation = '', 
                                is_wheelchair_accessible = True, ), ), 
                        notes = [
                            openapi_client.models.vt/api_planera_resa/core/models/note.VT.ApiPlaneraResa.Core.Models.Note(
                                type = '', 
                                text = '', )
                            ], 
                        estimated_distance_in_meters = 56, 
                        planned_connecting_time_in_minutes = 56, 
                        estimated_connecting_time_in_minutes = 56, 
                        is_risk_of_missing_connection = True, 
                        planned_departure_time = '', 
                        planned_arrival_time = '', 
                        planned_duration_in_minutes = 56, 
                        estimated_departure_time = '', 
                        estimated_arrival_time = '', 
                        estimated_duration_in_minutes = 56, 
                        estimated_otherwise_planned_arrival_time = '', 
                        estimated_otherwise_planned_departure_time = '', 
                        occupancy = openapi_client.models.vt/api_planera_resa/web/v4/models/occupancy_information_api_model.VT.ApiPlaneraResa.Web.V4.Models.OccupancyInformationApiModel(
                            level = 'low', 
                            source = 'prediction', ), 
                        journey_leg_index = 56, )
                    ],
                connection_links = [
                    openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/connection_link_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.ConnectionLinkApiModel(
                        transport_mode = 'unknown', 
                        transport_sub_mode = 'unknown', 
                        origin = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/call_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.CallApiModel(
                            stop_point = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/stop_point_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.StopPointApiModel(
                                gid = '0', 
                                name = '0', 
                                platform = '', 
                                latitude = 1.337, 
                                longitude = 1.337, 
                                stop_area = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/stop_area_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.StopAreaApiModel(
                                    gid = '', 
                                    name = '', 
                                    latitude = 1.337, 
                                    longitude = 1.337, 
                                    tariff_zone1 = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/tariff_zone_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.TariffZoneApiModel(
                                        gid = '', 
                                        name = '', 
                                        number = 56, 
                                        short_name = '', ), 
                                    tariff_zone2 = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/tariff_zone_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.TariffZoneApiModel(
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
                                ], ), 
                        destination = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/call_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.CallApiModel(
                            stop_point = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/stop_point_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.StopPointApiModel(
                                gid = '0', 
                                name = '0', 
                                platform = '', 
                                latitude = 1.337, 
                                longitude = 1.337, ), 
                            planned_time = '0', 
                            estimated_time = '', 
                            estimated_otherwise_planned_time = '', ), 
                        notes = [
                            openapi_client.models.vt/api_planera_resa/core/models/note.VT.ApiPlaneraResa.Core.Models.Note(
                                type = '', 
                                text = '', )
                            ], 
                        distance_in_meters = 56, 
                        planned_departure_time = '', 
                        planned_arrival_time = '', 
                        planned_duration_in_minutes = 56, 
                        estimated_departure_time = '', 
                        estimated_arrival_time = '', 
                        estimated_duration_in_minutes = 56, 
                        estimated_number_of_steps = 56, 
                        link_coordinates = [
                            openapi_client.models.vt/api_planera_resa/web/v4/models/coordinate_api_model.VT.ApiPlaneraResa.Web.V4.Models.CoordinateApiModel(
                                latitude = 1.337, 
                                longitude = 1.337, 
                                elevation = 1.337, 
                                is_on_trip_leg = True, 
                                is_trip_leg_start = True, 
                                is_trip_leg_stop = True, )
                            ], 
                        segments = [
                            openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/link_segment_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.LinkSegmentApiModel(
                                name = '', 
                                maneuver = 'none', 
                                orientation = 'unknown', 
                                maneuver_description = '', 
                                distance_in_meters = 56, )
                            ], 
                        journey_leg_index = 56, )
                    ],
                arrival_access_link = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/arrival_access_link_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.ArrivalAccessLinkApiModel(
                    transport_mode = 'unknown', 
                    transport_sub_mode = 'unknown', 
                    origin = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/call_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.CallApiModel(
                        stop_point = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/stop_point_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.StopPointApiModel(
                            gid = '0', 
                            name = '0', 
                            platform = '', 
                            latitude = 1.337, 
                            longitude = 1.337, 
                            stop_area = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/stop_area_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.StopAreaApiModel(
                                gid = '', 
                                name = '', 
                                latitude = 1.337, 
                                longitude = 1.337, 
                                tariff_zone1 = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/tariff_zone_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.TariffZoneApiModel(
                                    gid = '', 
                                    name = '', 
                                    number = 56, 
                                    short_name = '', ), 
                                tariff_zone2 = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/tariff_zone_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.TariffZoneApiModel(
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
                            ], ), 
                    destination = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/link_endpoint_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.LinkEndpointApiModel(
                        gid = '', 
                        name = '0', 
                        location_type = 'unknown', 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        planned_time = '0', 
                        estimated_time = '', 
                        estimated_otherwise_planned_time = '', ), 
                    notes = [
                        openapi_client.models.vt/api_planera_resa/core/models/note.VT.ApiPlaneraResa.Core.Models.Note(
                            type = '', 
                            text = '', )
                        ], 
                    distance_in_meters = 56, 
                    planned_departure_time = '', 
                    planned_arrival_time = '', 
                    planned_duration_in_minutes = 56, 
                    estimated_departure_time = '', 
                    estimated_arrival_time = '', 
                    estimated_duration_in_minutes = 56, 
                    estimated_number_of_steps = 56, 
                    link_coordinates = [
                        openapi_client.models.vt/api_planera_resa/web/v4/models/coordinate_api_model.VT.ApiPlaneraResa.Web.V4.Models.CoordinateApiModel(
                            latitude = 1.337, 
                            longitude = 1.337, 
                            elevation = 1.337, 
                            is_on_trip_leg = True, 
                            is_trip_leg_start = True, 
                            is_trip_leg_stop = True, )
                        ], 
                    segments = [
                        openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/link_segment_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.LinkSegmentApiModel(
                            name = '', 
                            maneuver = 'none', 
                            orientation = 'unknown', 
                            maneuver_description = '', 
                            distance_in_meters = 56, )
                        ], ),
                destination_link = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/destination_link_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.DestinationLinkApiModel(
                    transport_mode = 'unknown', 
                    transport_sub_mode = 'unknown', 
                    origin = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/link_endpoint_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.LinkEndpointApiModel(
                        gid = '', 
                        name = '0', 
                        location_type = 'unknown', 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        planned_time = '0', 
                        estimated_time = '', 
                        estimated_otherwise_planned_time = '', 
                        notes = [
                            openapi_client.models.vt/api_planera_resa/core/models/note.VT.ApiPlaneraResa.Core.Models.Note(
                                type = '', 
                                severity = 'unknown', 
                                text = '', )
                            ], ), 
                    destination = openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/link_endpoint_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.LinkEndpointApiModel(
                        gid = '', 
                        name = '0', 
                        location_type = 'unknown', 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        planned_time = '0', 
                        estimated_time = '', 
                        estimated_otherwise_planned_time = '', ), 
                    notes = [
                        openapi_client.models.vt/api_planera_resa/core/models/note.VT.ApiPlaneraResa.Core.Models.Note(
                            type = '', 
                            text = '', )
                        ], 
                    distance_in_meters = 56, 
                    planned_departure_time = '', 
                    planned_arrival_time = '', 
                    planned_duration_in_minutes = 56, 
                    estimated_departure_time = '', 
                    estimated_arrival_time = '', 
                    estimated_duration_in_minutes = 56, 
                    estimated_number_of_steps = 56, 
                    link_coordinates = [
                        openapi_client.models.vt/api_planera_resa/web/v4/models/coordinate_api_model.VT.ApiPlaneraResa.Web.V4.Models.CoordinateApiModel(
                            latitude = 1.337, 
                            longitude = 1.337, 
                            elevation = 1.337, 
                            is_on_trip_leg = True, 
                            is_trip_leg_start = True, 
                            is_trip_leg_stop = True, )
                        ], 
                    segments = [
                        openapi_client.models.vt/api_planera_resa/web/v4/models/journeys/link_segment_api_model.VT.ApiPlaneraResa.Web.V4.Models.Journeys.LinkSegmentApiModel(
                            name = '', 
                            maneuver = 'none', 
                            orientation = 'unknown', 
                            maneuver_description = '', 
                            distance_in_meters = 56, )
                        ], ),
                is_departed = True,
                occupancy = openapi_client.models.vt/api_planera_resa/web/v4/models/occupancy_information_api_model.VT.ApiPlaneraResa.Web.V4.Models.OccupancyInformationApiModel(
                    level = 'low', 
                    source = 'prediction', )
            )
        else:
            return VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel(
        )
        """

    def testVTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel(self):
        """Test VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
