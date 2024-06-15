from dataclasses import dataclass

from generated.equipment_position_structure import EquipmentPositionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EquipmentPosition(EquipmentPositionStructure):
    """
    The precise position within an EQUIPMENT PLACE where particular EQUIPMENT is
    placed.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
