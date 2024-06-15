from dataclasses import dataclass

from generated.equipment_ref_structure import EquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EquipmentRef(EquipmentRefStructure):
    """
    Reference to EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
