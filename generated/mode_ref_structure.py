from dataclasses import dataclass, field

from generated.all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from generated.submode_ref_structure import SubmodeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ModeRefStructure(SubmodeRefStructure):
    """
    Type for a reference to a MODE and SUBMODE.
    """

    mode: AllVehicleModesOfTransportEnumeration = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
