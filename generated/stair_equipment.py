from dataclasses import dataclass

from generated.stair_equipment_version_structure import (
    StairEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StairEquipment(StairEquipmentVersionStructure):
    """
    Specialisation of ACCESS EQUIPMENT for stairs (stair, escalator, staircase,
    etc.).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
