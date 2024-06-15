from dataclasses import dataclass

from generated.place_equipment_version_structure import (
    PlaceEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceEquipment(PlaceEquipmentVersionStructure):
    """
    An item of equipment of a particular type actually available at a location
    within a PLACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
