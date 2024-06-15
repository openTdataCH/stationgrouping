from dataclasses import dataclass

from generated.escalator_equipment_version_structure import (
    EscalatorEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EscalatorEquipment(EscalatorEquipmentVersionStructure):
    """
    Specialisation of STAIR EQUIPMENT for ESCALATORs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
