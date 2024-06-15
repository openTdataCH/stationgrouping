from dataclasses import dataclass

from generated.staircase_equipment_ref_structure import (
    StaircaseEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StaircaseEquipmentRef(StaircaseEquipmentRefStructure):
    """
    Identifier of an STAIRCASE EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
