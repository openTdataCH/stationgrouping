from dataclasses import dataclass

from generated.trolley_stand_equipment_ref_structure import (
    TrolleyStandEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrolleyStandEquipmentRef(TrolleyStandEquipmentRefStructure):
    """
    Identifier of an TROLLEY STAND EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
