from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.fare_demand_factor_ref import FareDemandFactorRef
from generated.fare_quota_factor_ref import FareQuotaFactorRef
from generated.fare_structure_factor import FareStructureFactor
from generated.geographical_structure_factor_ref import (
    GeographicalStructureFactorRef,
)
from generated.parking_charge_band_ref import ParkingChargeBandRef
from generated.quality_structure_factor_ref import QualityStructureFactorRef
from generated.time_structure_factor_ref import TimeStructureFactorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureFactorsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FARE STRUCTURE FACTORs.
    """

    class Meta:
        name = "fareStructureFactors_RelStructure"

    choice: List[
        Union[
            ParkingChargeBandRef,
            TimeStructureFactorRef,
            FareQuotaFactorRef,
            FareDemandFactorRef,
            QualityStructureFactorRef,
            GeographicalStructureFactorRef,
            FareStructureFactor,
        ]
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
                    "name": "TimeStructureFactorRef",
                    "type": TimeStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareQuotaFactorRef",
                    "type": FareQuotaFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactorRef",
                    "type": FareDemandFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorRef",
                    "type": QualityStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalStructureFactorRef",
                    "type": GeographicalStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureFactor",
                    "type": FareStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
