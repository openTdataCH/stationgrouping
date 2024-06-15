from dataclasses import dataclass

from generated.installed_equipment_version_structure import (
    InstalledEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    """
    Type for a PLACE EQUIPMENT.
    """

    class Meta:
        name = "PlaceEquipment_VersionStructure"
