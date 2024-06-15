from dataclasses import dataclass, field
from typing import List, Union

from generated.fare_demand_factor import FareDemandFactor
from generated.fare_demand_factor_ref import FareDemandFactorRef
from generated.fare_quota_factor import FareQuotaFactor
from generated.fare_quota_factor_ref import FareQuotaFactorRef
from generated.quality_structure_factor import QualityStructureFactor
from generated.quality_structure_factor_ref import QualityStructureFactorRef
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QualityStructureFactorsRelStructure(
    StrictContainmentAggregationStructure
):
    """
    Type for a list of QUALITY STRUCTURE FACTOR.
    """

    class Meta:
        name = "qualityStructureFactors_RelStructure"

    choice: List[
        Union[
            FareQuotaFactorRef,
            FareDemandFactorRef,
            QualityStructureFactorRef,
            FareQuotaFactor,
            FareDemandFactor,
            QualityStructureFactor,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
                    "name": "FareQuotaFactor",
                    "type": FareQuotaFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactor",
                    "type": FareDemandFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactor",
                    "type": QualityStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
