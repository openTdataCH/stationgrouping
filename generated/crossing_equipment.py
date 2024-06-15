from dataclasses import dataclass

from generated.crossing_equipment_version_structure import (
    CrossingEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CrossingEquipment(CrossingEquipmentVersionStructure):
    """
    Specialisation of PLACE ACCESS EQUIPMENT for CROSSING EQUIPMENTs (zebra,
    pedestrian lights, acoustic device sensors, tactile guide strips, etc.).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
