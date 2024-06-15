from dataclasses import dataclass, field
from typing import Optional

from generated.equipment_positions_rel_structure import (
    EquipmentPositionsRelStructure,
)
from generated.equipments_rel_structure import EquipmentsRelStructure
from generated.place_version_structure import PlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EquipmentPlaceVersionStructure(PlaceVersionStructure):
    """
    Type for an EQUIPMENT PLACE.

    :ivar equipment_positions: Positions of EQUIPMENT.
    :ivar place_equipments: Items of EQUIPMENT that may be located in an
        EQUIPMENT PLACE.
    """

    class Meta:
        name = "EquipmentPlace_VersionStructure"

    equipment_positions: Optional[EquipmentPositionsRelStructure] = field(
        default=None,
        metadata={
            "name": "equipmentPositions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    place_equipments: Optional[EquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "placeEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
