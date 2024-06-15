from dataclasses import dataclass

from generated.activated_equipment_ref_structure import (
    ActivatedEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivatedEquipmentRef(ActivatedEquipmentRefStructure):
    """
    Reference to an ACTIVATED EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
