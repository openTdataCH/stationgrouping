from dataclasses import dataclass

from generated.lift_equipment_version_structure import (
    LiftEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LiftEquipment(LiftEquipmentVersionStructure):
    """
    Specialisation of PLACE ACCESS EQUIPMENT for LIFTs (provides lift
    characteristics like depth, maximum load, etc.).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
