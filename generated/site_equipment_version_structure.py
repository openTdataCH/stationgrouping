from dataclasses import dataclass

from generated.installed_equipment_version_structure import (
    InstalledEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    """
    Type for a SITE EQUIPMENT.
    """

    class Meta:
        name = "SiteEquipment_VersionStructure"
