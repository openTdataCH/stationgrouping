from dataclasses import dataclass, field
from typing import Optional

from generated.all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from generated.place_ref_structure import PlaceRefStructure
from generated.point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessEndStructure:
    """
    Type for ACCESS link end.

    :ivar transport_mode: Identifier of MODE of end point of ACCESS
        link. Default is all modes.
    :ivar place_ref: Identifier of a PLACE at end point of ACCESS link.
    :ivar point_ref: Identifier of end point of ACCESS link.
    """

    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    place_ref: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "PointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
