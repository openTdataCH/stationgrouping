from dataclasses import dataclass

from generated.type_of_equipment_value_structure import (
    TypeOfEquipmentValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfEquipment(TypeOfEquipmentValueStructure):
    """
    A classification of a EQUIPMENT according to its functional purpose.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
