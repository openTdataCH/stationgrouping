from dataclasses import dataclass

from generated.luggage_locker_equipment_version_structure import (
    LuggageLockerEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageLockerEquipment(LuggageLockerEquipmentVersionStructure):
    """
    Specialisation of SITE EQUIPMENT for LUGGAGE LOCKERs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
