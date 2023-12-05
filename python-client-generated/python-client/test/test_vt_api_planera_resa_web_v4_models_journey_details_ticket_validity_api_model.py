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

from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_ticket_validity_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel  # noqa: E501

class TestVTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel(unittest.TestCase):
    """VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel:
        """Test VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel`
        """
        model = VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel()  # noqa: E501
        if include_optional:
            return VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel(
                id = '',
                is_valid_for_journey = True
            )
        else:
            return VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel(
        )
        """

    def testVTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel(self):
        """Test VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
