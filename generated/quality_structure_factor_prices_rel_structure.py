from dataclasses import dataclass, field
from typing import List, Union

from generated.cell_ref import CellRef
from generated.quality_structure_factor_price_ref import (
    QualityStructureFactorPriceRef,
)
from generated.quality_structure_factor_price_versioned_child_structure import (
    QualityStructureFactorPriceVersionedChildStructure,
)
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QualityStructureFactorPricesRelStructure(
    StrictContainmentAggregationStructure
):
    """
    Type for a list of QUALITY STRUCTURE FACTOR PRICEs.
    """

    class Meta:
        name = "qualityStructureFactorPrices_RelStructure"

    quality_structure_factor_price_ref_or_quality_structure_factor_price_or_cell_ref: List[
        Union[
            QualityStructureFactorPriceRef,
            QualityStructureFactorPriceVersionedChildStructure,
            CellRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "QualityStructureFactorPriceRef",
                    "type": QualityStructureFactorPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPrice",
                    "type": QualityStructureFactorPriceVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
