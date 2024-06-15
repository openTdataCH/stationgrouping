from dataclasses import dataclass, field
from typing import Optional

from generated.installed_equipment_version_structure import (
    InstalledEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    """
    Type for a PASSENGER EQUIPMENT.

    :ivar fixed: Whether the EQUIPMENT is fixed at a place or min a
        vehicle.
    """

    class Meta:
        name = "PassengerEquipment_VersionStructure"

    fixed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Fixed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
