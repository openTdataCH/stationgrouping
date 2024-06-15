from dataclasses import dataclass, field
from typing import List, Optional, Union

from generated.air_submode import AirSubmode
from generated.bus_submode import BusSubmode
from generated.coach_submode import CoachSubmode
from generated.funicular_submode import FunicularSubmode
from generated.metro_submode import MetroSubmode
from generated.rail_submode import RailSubmode
from generated.site_entrance_version_structure import (
    SiteEntranceVersionStructure,
)
from generated.snow_and_ice_submode import SnowAndIceSubmode
from generated.tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from generated.telecabin_submode import TelecabinSubmode
from generated.tram_submode import TramSubmode
from generated.vehicle_mode_enumeration import VehicleModeEnumeration
from generated.water_submode import WaterSubmode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceEntranceVersionStructure(SiteEntranceVersionStructure):
    """
    Type for Passenger STOP PLACE ENTRANCE.

    :ivar transport_mode: Primary MODE of Vehicle transport associated
        by this component.
    :ivar choice:
    :ivar other_transport_modes: Public transport MODES which may be
        accessed through associated place.
    :ivar tariff_zones: TARIFF ZONEs into which component falls.
    """

    class Meta:
        name = "StopPlaceEntrance_VersionStructure"

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
    other_transport_modes: List[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "OtherTransportModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    tariff_zones: Optional[TariffZoneRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "tariffZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
