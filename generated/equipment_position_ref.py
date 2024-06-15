from dataclasses import dataclass

from generated.equipment_position_ref_structure import (
    EquipmentPositionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EquipmentPositionRef(EquipmentPositionRefStructure):
    """
    Reference to an EQUIPMENT POSITION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
