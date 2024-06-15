from dataclasses import dataclass

from generated.waiting_equipment_version_structure import (
    WaitingEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WaitingEquipment(WaitingEquipmentVersionStructure):
    """
    Specialisation of SITE EQUIPMENT for WAITING EQUIPMENTs (shelter, waiting room,
    etc.).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
