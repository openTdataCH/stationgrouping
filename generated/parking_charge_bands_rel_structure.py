from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.parking_charge_band_ref import ParkingChargeBandRef
from generated.priceable_object_version_structure import ParkingChargeBand

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingChargeBandsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of PARKING TARIFF CHARGE BANDs.
    """

    class Meta:
        name = "parkingChargeBands_RelStructure"

    parking_charge_band_ref_or_parking_charge_band: List[
        Union[ParkingChargeBandRef, ParkingChargeBand]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingChargeBandRef",
                    "type": ParkingChargeBandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingChargeBand",
                    "type": ParkingChargeBand,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
