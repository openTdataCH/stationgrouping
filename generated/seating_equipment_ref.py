from dataclasses import dataclass

from generated.seating_equipment_ref_structure import (
    SeatingEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeatingEquipmentRef(SeatingEquipmentRefStructure):
    """
    Identifier of an SEATING EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
