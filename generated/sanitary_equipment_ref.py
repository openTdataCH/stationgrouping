from dataclasses import dataclass

from generated.sanitary_equipment_ref_structure import (
    SanitaryEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SanitaryEquipmentRef(SanitaryEquipmentRefStructure):
    """
    Identifier of an SANITARY FACILITY EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
