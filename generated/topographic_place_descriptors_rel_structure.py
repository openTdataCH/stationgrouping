from dataclasses import dataclass, field
from typing import List

from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from generated.topographic_place_descriptor_versioned_child_structure import (
    TopographicPlaceDescriptorVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicPlaceDescriptorsRelStructure(
    StrictContainmentAggregationStructure
):
    """
    Type for containment of TOPOGRAPHIC PLACE DESCRIPTORs.
    """

    class Meta:
        name = "topographicPlaceDescriptors_RelStructure"

    topographic_place_descriptor: List[
        TopographicPlaceDescriptorVersionedChildStructure
    ] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceDescriptor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
