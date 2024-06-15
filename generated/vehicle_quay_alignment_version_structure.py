from dataclasses import dataclass, field
from typing import Optional

from generated.entity_in_version_structure import VersionedChildStructure
from generated.quay_ref import QuayRef
from generated.vehicle_stopping_place_ref import VehicleStoppingPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleQuayAlignmentVersionStructure(VersionedChildStructure):
    """
    Type for a VEHICLE QUAY ALIGNMENT.

    :ivar vehicle_stopping_place_ref:
    :ivar quay_ref:
    :ivar order: Order of element.
    """

    class Meta:
        name = "VehicleQuayAlignment_VersionStructure"

    vehicle_stopping_place_ref: Optional[VehicleStoppingPlaceRef] = field(
        default=None,
        metadata={
            "name": "VehicleStoppingPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quay_ref: QuayRef = field(
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
