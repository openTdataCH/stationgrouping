from dataclasses import dataclass, field
from typing import List, Union

from generated.check_constraint_throughput import CheckConstraintThroughput
from generated.check_constraint_throughput_ref import (
    CheckConstraintThroughputRef,
)
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CheckConstraintThroughputsRelStructure(
    StrictContainmentAggregationStructure
):
    """
    A collection of one or more CHECK CONSTRAINTs.
    """

    class Meta:
        name = "checkConstraintThroughputs_RelStructure"

    check_constraint_throughput_ref_or_check_constraint_throughput: List[
        Union[CheckConstraintThroughputRef, CheckConstraintThroughput]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CheckConstraintThroughputRef",
                    "type": CheckConstraintThroughputRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CheckConstraintThroughput",
                    "type": CheckConstraintThroughput,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
