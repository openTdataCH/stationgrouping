from dataclasses import dataclass

from generated.entrance_equipment_version_structure import (
    EntranceEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntranceEquipment(EntranceEquipmentVersionStructure):
    """
    Specialisation of PLACE ACCESS EQUIPMENT for ENTRANCEs (door, barrier,
    revolving door, etc.).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
