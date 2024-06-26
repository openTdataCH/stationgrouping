from dataclasses import dataclass

from generated.access_equipment_ref_structure import (
    AccessEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StaircaseEquipmentRefStructure(AccessEquipmentRefStructure):
    """
    Type for a reference to an STAIRCASE EQUIPMENT.
    """
