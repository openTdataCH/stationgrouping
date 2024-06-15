from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from generated.parking_component_version_structure import (
    ParkingComponentVersionStructure,
)
from generated.parking_vehicle_enumeration import ParkingVehicleEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingBayVersionStructure(ParkingComponentVersionStructure):
    """
    Type for a PARKING BAY.

    :ivar parking_vehicle_type: Type of vehicle in PARKING BAY.
    :ivar length: Length of PARKING BAY.
    :ivar width: Width of PARKING BAY.
    :ivar height: Height of PARKING BAY.
    :ivar weight: Maximum Weight allowed in PARKING BAY. +v1.1
    :ivar recharging_available: Whether power for recharging. See
        Equipment for details.
    """

    class Meta:
        name = "ParkingBay_VersionStructure"

    parking_vehicle_type: Optional[ParkingVehicleEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingVehicleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    recharging_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RechargingAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
