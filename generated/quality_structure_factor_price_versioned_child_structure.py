from dataclasses import dataclass, field
from typing import Optional, Union

from generated.fare_demand_factor_ref import FareDemandFactorRef
from generated.fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)
from generated.fare_quota_factor_ref import FareQuotaFactorRef
from generated.quality_structure_factor_ref import QualityStructureFactorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QualityStructureFactorPriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    """
    Type for a QUALITY STRUCTURE FACTOR PRICEs.
    """

    class Meta:
        name = "QualityStructureFactorPrice_VersionedChildStructure"

    fare_quota_factor_ref_or_fare_demand_factor_ref_or_quality_structure_factor_ref: Optional[
        Union[
            FareQuotaFactorRef, FareDemandFactorRef, QualityStructureFactorRef
        ]
    ] = field(
        default=None,
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
            ),
        },
    )
