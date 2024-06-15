from dataclasses import dataclass

from generated.travelator_equipment_ref_structure import (
    TravelatorEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelatorEquipmentRef(TravelatorEquipmentRefStructure):
    """
    Identifier of an ENTRANCE EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
