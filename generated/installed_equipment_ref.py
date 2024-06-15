from dataclasses import dataclass

from generated.installed_equipment_ref_structure import (
    InstalledEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InstalledEquipmentRef(InstalledEquipmentRefStructure):
    """
    Reference to an INSTALLED EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
