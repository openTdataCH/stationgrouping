from dataclasses import dataclass, field
from typing import Optional

from generated.boarding_position_ref import BoardingPositionRef
from generated.entity_in_version_structure import VersionedChildStructure
from generated.stop_place_entrance_ref import StopPlaceEntranceRef
from generated.vehicle_stopping_position_ref import VehicleStoppingPositionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePositionAlignmentVersionStructure(VersionedChildStructure):
    """
    Type for a VEHICLE POSTION ALIGNMENT.

    :ivar vehicle_stopping_position_ref:
    :ivar boarding_position_ref:
    :ivar stop_place_entrance_ref:
    :ivar order: Order of attribute
    """

    class Meta:
        name = "VehiclePositionAlignment_VersionStructure"

    vehicle_stopping_position_ref: Optional[VehicleStoppingPositionRef] = (
        field(
            default=None,
            metadata={
                "name": "VehicleStoppingPositionRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    boarding_position_ref: Optional[BoardingPositionRef] = field(
        default=None,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_place_entrance_ref: Optional[StopPlaceEntranceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
