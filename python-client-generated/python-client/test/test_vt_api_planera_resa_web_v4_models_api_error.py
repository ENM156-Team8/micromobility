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

from openapi_client.models.vt_api_planera_resa_web_v4_models_api_error import VTApiPlaneraResaWebV4ModelsApiError  # noqa: E501

class TestVTApiPlaneraResaWebV4ModelsApiError(unittest.TestCase):
    """VTApiPlaneraResaWebV4ModelsApiError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VTApiPlaneraResaWebV4ModelsApiError:
        """Test VTApiPlaneraResaWebV4ModelsApiError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VTApiPlaneraResaWebV4ModelsApiError`
        """
        model = VTApiPlaneraResaWebV4ModelsApiError()  # noqa: E501
        if include_optional:
            return VTApiPlaneraResaWebV4ModelsApiError(
                error_code = 56,
                error_message = ''
            )
        else:
            return VTApiPlaneraResaWebV4ModelsApiError(
        )
        """

    def testVTApiPlaneraResaWebV4ModelsApiError(self):
        """Test VTApiPlaneraResaWebV4ModelsApiError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
