from dataclasses import dataclass

from generated.installed_equipment_version_structure import (
    InstalledEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InstalledEquipment(InstalledEquipmentVersionStructure):
    """
    INSTALLED EQUIPMENT describes the different types of LOCATED EQUIPMENT that may
    be associated with the SITE COMPONENTs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
