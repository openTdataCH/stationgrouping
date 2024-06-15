from dataclasses import dataclass

from generated.trolley_stand_equipment_version_structure import (
    TrolleyStandEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrolleyStandEquipment(TrolleyStandEquipmentVersionStructure):
    """
    Specialisation of SITE EQUIPMENT for TROLLEY STANDs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
