from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.sections_in_sequence_rel_structure import CommonSection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommonSectionsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of COMMON SECTION.
    """

    class Meta:
        name = "commonSectionsInFrame_RelStructure"

    common_section: List[CommonSection] = field(
        default_factory=list,
        metadata={
            "name": "CommonSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
