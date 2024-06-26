from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.equipment_place import EquipmentPlace
from generated.equipment_place_ref import EquipmentPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EquipmentPlacesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of EQUIPMENT PLACEs.
    """

    class Meta:
        name = "equipmentPlaces_RelStructure"

    equipment_place_ref_or_equipment_place: List[
        Union[EquipmentPlaceRef, EquipmentPlace]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EquipmentPlaceRef",
                    "type": EquipmentPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentPlace",
                    "type": EquipmentPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
