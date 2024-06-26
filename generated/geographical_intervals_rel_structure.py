from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.geographical_interval import GeographicalInterval
from generated.geographical_interval_ref import GeographicalIntervalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalIntervalsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of GEOGRAPHICAL INTERVALs.
    """

    class Meta:
        name = "geographicalIntervals_RelStructure"

    geographical_interval_ref_or_geographical_interval: List[
        Union[GeographicalIntervalRef, GeographicalInterval]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeographicalIntervalRef",
                    "type": GeographicalIntervalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalInterval",
                    "type": GeographicalInterval,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
