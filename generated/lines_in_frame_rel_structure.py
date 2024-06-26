from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.flexible_line import FlexibleLine
from generated.line import Line

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of LINe.
    """

    class Meta:
        name = "linesInFrame_RelStructure"

    flexible_line_or_line: List[Union[FlexibleLine, Line]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLine",
                    "type": FlexibleLine,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Line",
                    "type": Line,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
