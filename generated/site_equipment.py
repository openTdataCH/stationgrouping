from dataclasses import dataclass

from generated.site_equipment_version_structure import (
    SiteEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteEquipment(SiteEquipmentVersionStructure):
    """
    Specialisation of PLACE EQUIPMENT for SITEs (e.g. LUGGAGE LOCKER, WAITING
    EQUIPMENT, TROLLEY STAND, etc.)
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
