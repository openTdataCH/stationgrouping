from dataclasses import dataclass

from generated.seating_equipment_version_structure import (
    SeatingEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeatingEquipment(SeatingEquipmentVersionStructure):
    """
    Specialisation of WAITING EQUIPMENT describing the properties of seating.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
