from dataclasses import dataclass, field
from typing import Optional

from generated.entity_in_version_structure import VersionedChildStructure
from generated.parking_properties_ref import ParkingPropertiesRef
from generated.parking_properties_ref_structure import (
    ParkingPropertiesRefStructure,
)
from generated.parking_ref import ParkingRef
from generated.parking_stay_enumeration import ParkingStayEnumeration
from generated.parking_user_enumeration import ParkingUserEnumeration
from generated.parking_vehicle_enumeration import ParkingVehicleEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingCapacityVersionedChildStructure(VersionedChildStructure):
    """
    Type for a PARKING CAPACITY.

    :ivar parking_ref:
    :ivar parent_ref: DEPRECATED As not integrity checked.
    :ivar parking_properties_ref:
    :ivar parking_user_type: Type of users: disabled, all etc.
    :ivar parking_vehicle_type: Type of vehicle that PARKING allows.
    :ivar parking_stay_type: Type of Stay allowed in PARKING.
    :ivar number_of_spaces: Total number of parking places.
    :ivar number_of_spaces_with_recharge_point: Number of parking places
        with eletric chargepoints.
    """

    class Meta:
        name = "ParkingCapacity_VersionedChildStructure"

    parking_ref: Optional[ParkingRef] = field(
        default=None,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_ref: Optional[ParkingPropertiesRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_properties_ref: Optional[ParkingPropertiesRef] = field(
        default=None,
        metadata={
            "name": "ParkingPropertiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_user_type: Optional[ParkingUserEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingUserType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_vehicle_type: Optional[ParkingVehicleEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingVehicleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_stay_type: Optional[ParkingStayEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingStayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSpaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_spaces_with_recharge_point: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSpacesWithRechargePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
