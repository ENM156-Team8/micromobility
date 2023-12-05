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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from openapi_client.models.vt_api_planera_resa_core_models_note import VTApiPlaneraResaCoreModelsNote
from openapi_client.models.vt_api_planera_resa_core_models_transport_mode import VTApiPlaneraResaCoreModelsTransportMode
from openapi_client.models.vt_api_planera_resa_core_models_transport_sub_mode import VTApiPlaneraResaCoreModelsTransportSubMode
from openapi_client.models.vt_api_planera_resa_web_v4_models_coordinate_api_model import VTApiPlaneraResaWebV4ModelsCoordinateApiModel
from openapi_client.models.vt_api_planera_resa_web_v4_models_journeys_call_api_model import VTApiPlaneraResaWebV4ModelsJourneysCallApiModel
from openapi_client.models.vt_api_planera_resa_web_v4_models_journeys_link_segment_api_model import VTApiPlaneraResaWebV4ModelsJourneysLinkSegmentApiModel

class VTApiPlaneraResaWebV4ModelsJourneysConnectionLinkApiModel(BaseModel):
    """
    Information about a walk, bike or car link between two public transport trip legs.  # noqa: E501
    """
    transport_mode: Optional[VTApiPlaneraResaCoreModelsTransportMode] = Field(None, alias="transportMode")
    transport_sub_mode: Optional[VTApiPlaneraResaCoreModelsTransportSubMode] = Field(None, alias="transportSubMode")
    origin: Optional[VTApiPlaneraResaWebV4ModelsJourneysCallApiModel] = None
    destination: Optional[VTApiPlaneraResaWebV4ModelsJourneysCallApiModel] = None
    notes: Optional[conlist(VTApiPlaneraResaCoreModelsNote)] = Field(None, description="An ordered list (most important first) of notes related to the access link.")
    distance_in_meters: Optional[StrictInt] = Field(None, alias="distanceInMeters", description="Distance in meters.")
    planned_departure_time: Optional[StrictStr] = Field(None, alias="plannedDepartureTime", description="The planned departure time in RFC 3339 format.")
    planned_arrival_time: Optional[StrictStr] = Field(None, alias="plannedArrivalTime", description="The planned arrival time in RFC 3339 format.")
    planned_duration_in_minutes: Optional[StrictInt] = Field(None, alias="plannedDurationInMinutes", description="The planned duration in minutes.")
    estimated_departure_time: Optional[StrictStr] = Field(None, alias="estimatedDepartureTime", description="The estimated departure time in RFC 3339 format, if available.")
    estimated_arrival_time: Optional[StrictStr] = Field(None, alias="estimatedArrivalTime", description="The estimated arrival time in RFC 3339 format, if available.")
    estimated_duration_in_minutes: Optional[StrictInt] = Field(None, alias="estimatedDurationInMinutes", description="The estimated duration in minutes, if available.")
    estimated_number_of_steps: Optional[StrictInt] = Field(None, alias="estimatedNumberOfSteps", description="Number of steps based on the distance and an estimated step length of 0.65 meters.")
    link_coordinates: Optional[conlist(VTApiPlaneraResaWebV4ModelsCoordinateApiModel)] = Field(None, alias="linkCoordinates", description="The coordinates for the link.")
    segments: Optional[conlist(VTApiPlaneraResaWebV4ModelsJourneysLinkSegmentApiModel)] = Field(None, description="The segments that make up this link.")
    journey_leg_index: Optional[StrictInt] = Field(None, alias="journeyLegIndex", description="Index of Leg in Journey")
    __properties = ["transportMode", "transportSubMode", "origin", "destination", "notes", "distanceInMeters", "plannedDepartureTime", "plannedArrivalTime", "plannedDurationInMinutes", "estimatedDepartureTime", "estimatedArrivalTime", "estimatedDurationInMinutes", "estimatedNumberOfSteps", "linkCoordinates", "segments", "journeyLegIndex"]

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
    def from_json(cls, json_str: str) -> VTApiPlaneraResaWebV4ModelsJourneysConnectionLinkApiModel:
        """Create an instance of VTApiPlaneraResaWebV4ModelsJourneysConnectionLinkApiModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of origin
        if self.origin:
            _dict['origin'] = self.origin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination
        if self.destination:
            _dict['destination'] = self.destination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item in self.notes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in link_coordinates (list)
        _items = []
        if self.link_coordinates:
            for _item in self.link_coordinates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['linkCoordinates'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in segments (list)
        _items = []
        if self.segments:
            for _item in self.segments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['segments'] = _items
        # set to None if notes (nullable) is None
        # and __fields_set__ contains the field
        if self.notes is None and "notes" in self.__fields_set__:
            _dict['notes'] = None

        # set to None if distance_in_meters (nullable) is None
        # and __fields_set__ contains the field
        if self.distance_in_meters is None and "distance_in_meters" in self.__fields_set__:
            _dict['distanceInMeters'] = None

        # set to None if planned_departure_time (nullable) is None
        # and __fields_set__ contains the field
        if self.planned_departure_time is None and "planned_departure_time" in self.__fields_set__:
            _dict['plannedDepartureTime'] = None

        # set to None if planned_arrival_time (nullable) is None
        # and __fields_set__ contains the field
        if self.planned_arrival_time is None and "planned_arrival_time" in self.__fields_set__:
            _dict['plannedArrivalTime'] = None

        # set to None if planned_duration_in_minutes (nullable) is None
        # and __fields_set__ contains the field
        if self.planned_duration_in_minutes is None and "planned_duration_in_minutes" in self.__fields_set__:
            _dict['plannedDurationInMinutes'] = None

        # set to None if estimated_departure_time (nullable) is None
        # and __fields_set__ contains the field
        if self.estimated_departure_time is None and "estimated_departure_time" in self.__fields_set__:
            _dict['estimatedDepartureTime'] = None

        # set to None if estimated_arrival_time (nullable) is None
        # and __fields_set__ contains the field
        if self.estimated_arrival_time is None and "estimated_arrival_time" in self.__fields_set__:
            _dict['estimatedArrivalTime'] = None

        # set to None if estimated_duration_in_minutes (nullable) is None
        # and __fields_set__ contains the field
        if self.estimated_duration_in_minutes is None and "estimated_duration_in_minutes" in self.__fields_set__:
            _dict['estimatedDurationInMinutes'] = None

        # set to None if estimated_number_of_steps (nullable) is None
        # and __fields_set__ contains the field
        if self.estimated_number_of_steps is None and "estimated_number_of_steps" in self.__fields_set__:
            _dict['estimatedNumberOfSteps'] = None

        # set to None if link_coordinates (nullable) is None
        # and __fields_set__ contains the field
        if self.link_coordinates is None and "link_coordinates" in self.__fields_set__:
            _dict['linkCoordinates'] = None

        # set to None if segments (nullable) is None
        # and __fields_set__ contains the field
        if self.segments is None and "segments" in self.__fields_set__:
            _dict['segments'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VTApiPlaneraResaWebV4ModelsJourneysConnectionLinkApiModel:
        """Create an instance of VTApiPlaneraResaWebV4ModelsJourneysConnectionLinkApiModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VTApiPlaneraResaWebV4ModelsJourneysConnectionLinkApiModel.parse_obj(obj)

        _obj = VTApiPlaneraResaWebV4ModelsJourneysConnectionLinkApiModel.parse_obj({
            "transport_mode": obj.get("transportMode"),
            "transport_sub_mode": obj.get("transportSubMode"),
            "origin": VTApiPlaneraResaWebV4ModelsJourneysCallApiModel.from_dict(obj.get("origin")) if obj.get("origin") is not None else None,
            "destination": VTApiPlaneraResaWebV4ModelsJourneysCallApiModel.from_dict(obj.get("destination")) if obj.get("destination") is not None else None,
            "notes": [VTApiPlaneraResaCoreModelsNote.from_dict(_item) for _item in obj.get("notes")] if obj.get("notes") is not None else None,
            "distance_in_meters": obj.get("distanceInMeters"),
            "planned_departure_time": obj.get("plannedDepartureTime"),
            "planned_arrival_time": obj.get("plannedArrivalTime"),
            "planned_duration_in_minutes": obj.get("plannedDurationInMinutes"),
            "estimated_departure_time": obj.get("estimatedDepartureTime"),
            "estimated_arrival_time": obj.get("estimatedArrivalTime"),
            "estimated_duration_in_minutes": obj.get("estimatedDurationInMinutes"),
            "estimated_number_of_steps": obj.get("estimatedNumberOfSteps"),
            "link_coordinates": [VTApiPlaneraResaWebV4ModelsCoordinateApiModel.from_dict(_item) for _item in obj.get("linkCoordinates")] if obj.get("linkCoordinates") is not None else None,
            "segments": [VTApiPlaneraResaWebV4ModelsJourneysLinkSegmentApiModel.from_dict(_item) for _item in obj.get("segments")] if obj.get("segments") is not None else None,
            "journey_leg_index": obj.get("journeyLegIndex")
        })
        return _obj


