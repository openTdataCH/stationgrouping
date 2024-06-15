from dataclasses import dataclass

from generated.waiting_equipment_ref_structure import (
    WaitingEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WaitingEquipmentRef(WaitingEquipmentRefStructure):
    """
    Identifier of an WAITING EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
