from dataclasses import dataclass

from generated.equipment_version_structure import EquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InstalledEquipmentVersionStructure(EquipmentVersionStructure):
    """
    Type for INSTALLED EQUIPMENT.
    """

    class Meta:
        name = "InstalledEquipment_VersionStructure"
