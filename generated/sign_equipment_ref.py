from dataclasses import dataclass

from generated.equipment_ref_structure import EquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SignEquipmentRef(EquipmentRefStructure):
    """
    Identifier of an SIGN EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
