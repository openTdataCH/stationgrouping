from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.series_constraint import SeriesConstraint
from generated.series_constraint_ref import SeriesConstraintRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeriesConstraintsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of SERIES ELEMENTs.
    """

    class Meta:
        name = "SeriesConstraints_RelStructure"

    series_constraint_ref_or_series_constraint: List[
        Union[SeriesConstraintRef, SeriesConstraint]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SeriesConstraintRef",
                    "type": SeriesConstraintRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraint",
                    "type": SeriesConstraint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
