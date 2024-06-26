from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.passenger_information_equipment import (
    PassengerInformationEquipment,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerInformationEquipmentsInFrameRelStructure(
    ContainmentAggregationStructure
):
    """
    Type for containment in frame of PASS ENGER INFORMATION EQUIPMENT.
    """

    class Meta:
        name = "passengerInformationEquipmentsInFrame_RelStructure"

    passenger_information_equipment: List[PassengerInformationEquipment] = (
        field(
            default_factory=list,
            metadata={
                "name": "PassengerInformationEquipment",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
