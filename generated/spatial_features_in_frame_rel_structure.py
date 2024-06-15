from dataclasses import dataclass, field
from typing import List, Union

from generated.complex_feature import ComplexFeature
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.simple_feature import SimpleFeature

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpatialFeaturesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of TSPATIAL FEATURe.
    """

    class Meta:
        name = "spatialFeaturesInFrame_RelStructure"

    simple_feature_or_complex_feature: List[
        Union[SimpleFeature, ComplexFeature]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SimpleFeature",
                    "type": SimpleFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplexFeature",
                    "type": ComplexFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
