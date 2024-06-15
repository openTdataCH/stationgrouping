from dataclasses import dataclass, field
from typing import List, Union

from generated.check_constraint import CheckConstraint
from generated.check_constraint_ref import CheckConstraintRef
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CheckConstraintsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of CHECK CONSTRAINTs.
    """

    class Meta:
        name = "checkConstraints_RelStructure"

    check_constraint_ref_or_check_constraint: List[
        Union[CheckConstraintRef, CheckConstraint]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CheckConstraintRef",
                    "type": CheckConstraintRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CheckConstraint",
                    "type": CheckConstraint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
