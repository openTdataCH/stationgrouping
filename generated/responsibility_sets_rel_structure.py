from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.responsibility_set import ResponsibilitySet
from generated.responsibility_set_ref import ResponsibilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResponsibilitySetsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of RESPONSIBILITY SETs.
    """

    class Meta:
        name = "responsibilitySets_RelStructure"

    responsibility_set_ref_or_responsibility_set: List[
        Union[ResponsibilitySetRef, ResponsibilitySet]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ResponsibilitySetRef",
                    "type": ResponsibilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResponsibilitySet",
                    "type": ResponsibilitySet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
