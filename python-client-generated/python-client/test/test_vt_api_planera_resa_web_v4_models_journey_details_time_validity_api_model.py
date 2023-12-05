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

from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_details_time_validity_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel  # noqa: E501

class TestVTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel(unittest.TestCase):
    """VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel:
        """Test VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel`
        """
        model = VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel()  # noqa: E501
        if include_optional:
            return VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel(
                type = 'unknown',
                amount = 56,
                unit = 'unknown',
                from_date = '2018-11-29',
                to_date = '2018-11-30',
                from_date_time = '2018-11-30T17:07:10+01:00',
                to_date_time = '2018-11-30T17:07:10+01:00'
            )
        else:
            return VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel(
        )
        """

    def testVTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel(self):
        """Test VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
