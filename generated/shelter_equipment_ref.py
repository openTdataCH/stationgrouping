from dataclasses import dataclass

from generated.shelter_equipment_ref_structure import (
    ShelterEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ShelterEquipmentRef(ShelterEquipmentRefStructure):
    """
    Identifier of an SHELTER EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
