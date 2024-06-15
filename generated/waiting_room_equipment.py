from dataclasses import dataclass

from generated.waiting_room_equipment_version_structure import (
    WaitingRoomEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WaitingRoomEquipment(WaitingRoomEquipmentVersionStructure):
    """
    Specialisation of WAITING EQUIPMENT for WAITING ROOMs, classified by TYPE OF
    WAITING ROOM.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
