from dataclasses import dataclass, field
from typing import Optional

from generated.link_ref_by_value_structure import LinkRefByValueStructure
from generated.vehicle_mode import VehicleMode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ModalLinkRefByValueStructure(LinkRefByValueStructure):
    """
    Type for a reference to a LINK.
    """

    vehicle_mode: Optional[VehicleMode] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
