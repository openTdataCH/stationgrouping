from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.postal_address import PostalAddress
from generated.road_address import RoadAddress

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AddressesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of ADDRESSes.
    """

    class Meta:
        name = "addressesInFrame_RelStructure"

    postal_address_or_road_address: List[Union[PostalAddress, RoadAddress]] = (
        field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "PostalAddress",
                        "type": PostalAddress,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "RoadAddress",
                        "type": RoadAddress,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
