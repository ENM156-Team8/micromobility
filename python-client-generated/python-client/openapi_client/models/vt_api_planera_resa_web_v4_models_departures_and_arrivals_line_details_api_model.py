# coding: utf-8

"""
    Planera Resa

    Sök och planera resor med Västtrafik

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.vt_api_planera_resa_core_models_transport_mode import VTApiPlaneraResaCoreModelsTransportMode
from openapi_client.models.vt_api_planera_resa_core_models_transport_sub_mode import VTApiPlaneraResaCoreModelsTransportSubMode

class VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineDetailsApiModel(BaseModel):
    """
    Information about a line.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(None, description="The line name.")
    background_color: Optional[StrictStr] = Field(None, alias="backgroundColor", description="The background color of the line symbol.")
    foreground_color: Optional[StrictStr] = Field(None, alias="foregroundColor", description="The foreground color of the line symbol.")
    border_color: Optional[StrictStr] = Field(None, alias="borderColor", description="The border color of the line symbol.")
    transport_mode: Optional[VTApiPlaneraResaCoreModelsTransportMode] = Field(None, alias="transportMode")
    transport_sub_mode: Optional[VTApiPlaneraResaCoreModelsTransportSubMode] = Field(None, alias="transportSubMode")
    __properties = ["name", "backgroundColor", "foregroundColor", "borderColor", "transportMode", "transportSubMode"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineDetailsApiModel:
        """Create an instance of VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineDetailsApiModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if background_color (nullable) is None
        # and __fields_set__ contains the field
        if self.background_color is None and "background_color" in self.__fields_set__:
            _dict['backgroundColor'] = None

        # set to None if foreground_color (nullable) is None
        # and __fields_set__ contains the field
        if self.foreground_color is None and "foreground_color" in self.__fields_set__:
            _dict['foregroundColor'] = None

        # set to None if border_color (nullable) is None
        # and __fields_set__ contains the field
        if self.border_color is None and "border_color" in self.__fields_set__:
            _dict['borderColor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineDetailsApiModel:
        """Create an instance of VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineDetailsApiModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineDetailsApiModel.parse_obj(obj)

        _obj = VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineDetailsApiModel.parse_obj({
            "name": obj.get("name"),
            "background_color": obj.get("backgroundColor"),
            "foreground_color": obj.get("foregroundColor"),
            "border_color": obj.get("borderColor"),
            "transport_mode": obj.get("transportMode"),
            "transport_sub_mode": obj.get("transportSubMode")
        })
        return _obj


