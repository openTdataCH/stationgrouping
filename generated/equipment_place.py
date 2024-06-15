from dataclasses import dataclass

from generated.equipment_place_version_structure import (
    EquipmentPlaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EquipmentPlace(EquipmentPlaceVersionStructure):
    """
    Designated Place within a SITE for a locating EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
