from dataclasses import dataclass

from generated.entrance_equipment_ref_structure import (
    EntranceEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntranceEquipmentRef(EntranceEquipmentRefStructure):
    """
    Identifier of an ENTRANCE EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
