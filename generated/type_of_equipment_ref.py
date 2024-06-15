from dataclasses import dataclass

from generated.type_of_equipment_ref_structure import (
    TypeOfEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfEquipmentRef(TypeOfEquipmentRefStructure):
    """
    Reference to a TYPE OF EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
