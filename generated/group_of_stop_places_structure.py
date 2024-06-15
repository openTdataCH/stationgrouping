from dataclasses import dataclass, field
from typing import Optional, Union

from generated.air_submode import AirSubmode
from generated.alternative_names_rel_structure import (
    AlternativeNamesRelStructure,
)
from generated.bus_submode import BusSubmode
from generated.coach_submode import CoachSubmode
from generated.funicular_submode import FunicularSubmode
from generated.group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from generated.metro_submode import MetroSubmode
from generated.polygon import Polygon
from generated.rail_submode import RailSubmode
from generated.simple_point_version_structure import (
    SimplePointVersionStructure,
)
from generated.snow_and_ice_submode import SnowAndIceSubmode
from generated.stop_place_refs_rel_structure import StopPlaceRefsRelStructure
from generated.telecabin_submode import TelecabinSubmode
from generated.tram_submode import TramSubmode
from generated.vehicle_mode_enumeration import VehicleModeEnumeration
from generated.water_submode import WaterSubmode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfStopPlacesStructure(GroupOfEntitiesVersionStructure):
    """
    Type for GROUP of STOP PLACEs.

    :ivar public_code:
    :ivar members: Stations and stops in GROUP of STOP PLACEs.
    :ivar alternative_names: Alternative names for the GROUP of STOP
        PLACEs.
    :ivar centroid: Centre Coordinates of GROUP of STOP PLACEs.
    :ivar polygon:
    :ivar transport_mode: Primary MODE of Vehicle transport associated
        by this component.
    :ivar choice:
    """

    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: Optional[StopPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    centroid: Optional[SimplePointVersionStructure] = field(
        default=None,
        metadata={
            "name": "Centroid",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    transport_mode: Optional[VehicleModeEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            AirSubmode,
            BusSubmode,
            CoachSubmode,
            FunicularSubmode,
            MetroSubmode,
            TramSubmode,
            TelecabinSubmode,
            RailSubmode,
            WaterSubmode,
            SnowAndIceSubmode,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AirSubmode",
                    "type": AirSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BusSubmode",
                    "type": BusSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CoachSubmode",
                    "type": CoachSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FunicularSubmode",
                    "type": FunicularSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MetroSubmode",
                    "type": MetroSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TramSubmode",
                    "type": TramSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TelecabinSubmode",
                    "type": TelecabinSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailSubmode",
                    "type": RailSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaterSubmode",
                    "type": WaterSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SnowAndIceSubmode",
                    "type": SnowAndIceSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
