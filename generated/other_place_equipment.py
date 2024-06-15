from dataclasses import dataclass

from generated.place_equipment_version_structure import (
    PlaceEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherPlaceEquipment(PlaceEquipmentVersionStructure):
    """
    Equipment that may be in a fixed within a SITE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
