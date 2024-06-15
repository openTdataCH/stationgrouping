from dataclasses import dataclass, field
from typing import List, Union

from generated.access import Access
from generated.access_ref import AccessRef
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of ACCESS Links.
    """

    class Meta:
        name = "accesses_RelStructure"

    access_ref_or_access: List[Union[AccessRef, Access]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccessRef",
                    "type": AccessRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Access",
                    "type": Access,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
