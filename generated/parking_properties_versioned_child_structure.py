from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDuration

from generated.entity_in_version_structure import VersionedChildStructure
from generated.parking_area_refs_rel_structure import (
    ParkingAreaRefsRelStructure,
)
from generated.parking_capacities_rel_structure import (
    ParkingCapacitiesRelStructure,
)
from generated.parking_ref import ParkingRef
from generated.parking_stay_enumeration import ParkingStayEnumeration
from generated.parking_user_enumeration import ParkingUserEnumeration
from generated.parking_vehicle_enumeration import ParkingVehicleEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPropertiesVersionedChildStructure(VersionedChildStructure):
    """
    Type for a PARKING PROPERTies.

    :ivar parking_ref:
    :ivar parking_user_types: Type of users: disabled, all etc.
    :ivar parking_vehicle_types: Type of vehicle that PARKING allows.
    :ivar parking_stay_list: Nature of stay in PARKING.
    :ivar maximum_stay: Maximum allowed Stay as Duration.
    :ivar areas: PARKING AREA to which prperties appky +v1.1.
    :ivar spaces: Available spaces within PARKING AREA.
    """

    class Meta:
        name = "ParkingProperties_VersionedChildStructure"

    parking_ref: Optional[ParkingRef] = field(
        default=None,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_user_types: List[ParkingUserEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingUserTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    parking_vehicle_types: List[ParkingVehicleEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingVehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    parking_stay_list: List[ParkingStayEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingStayList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    maximum_stay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumStay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    areas: Optional[ParkingAreaRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    spaces: Optional[ParkingCapacitiesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
