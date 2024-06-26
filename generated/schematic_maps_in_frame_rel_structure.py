from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.schematic_map import SchematicMap

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SchematicMapsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of T SCHEMATIC MAPs.
    """

    class Meta:
        name = "schematicMapsInFrame_RelStructure"

    schematic_map: List[SchematicMap] = field(
        default_factory=list,
        metadata={
            "name": "SchematicMap",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
