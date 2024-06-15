from dataclasses import dataclass

from generated.access_equipment_version_structure import (
    AccessEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessEquipment(AccessEquipmentVersionStructure):
    """
    Specialisation of PLACE EQUIPMENT dedicated to access (e.g. lifts, entrances,
    stairs, ramps, etc.).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
