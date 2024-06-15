from dataclasses import dataclass

from generated.site_equipment_ref_structure import SiteEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteEquipmentRef(SiteEquipmentRefStructure):
    """
    Identifier of an SITE EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
