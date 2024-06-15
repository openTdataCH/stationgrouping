from dataclasses import dataclass

from generated.travelator_equipment_version_structure import (
    TravelatorEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelatorEquipment(TravelatorEquipmentVersionStructure):
    """
    Specialisation of PLACE EQUIPMENT for TRAVELATORs (provides travelator
    attributes like speed, etc.).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
