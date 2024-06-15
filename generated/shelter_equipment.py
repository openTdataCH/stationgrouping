from dataclasses import dataclass

from generated.shelter_equipment_version_structure import (
    ShelterEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ShelterEquipment(ShelterEquipmentVersionStructure):
    """
    Specialisation of WAITING EQUIPMENT for a SHELTER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
