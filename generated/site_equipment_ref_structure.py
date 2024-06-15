from dataclasses import dataclass

from generated.equipment_ref_structure import EquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteEquipmentRefStructure(EquipmentRefStructure):
    """
    Type for a reference to an SITE EQUIPMENT.
    """