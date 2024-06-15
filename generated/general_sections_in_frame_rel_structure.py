from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.sections_in_sequence_rel_structure import GeneralSection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralSectionsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of GENERAL SECTION.
    """

    class Meta:
        name = "generalSectionsInFrame_RelStructure"

    general_section: List[GeneralSection] = field(
        default_factory=list,
        metadata={
            "name": "GeneralSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
