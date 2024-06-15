from dataclasses import dataclass

from generated.staircase_equipment_version_structure import (
    StaircaseEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StaircaseEquipment(StaircaseEquipmentVersionStructure):
    """
    Specialisation of STAIR EQUIPMENT for stair cases.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
