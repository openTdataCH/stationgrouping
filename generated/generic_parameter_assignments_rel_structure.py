from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from generated.boolean_operator_enumeration import BooleanOperatorEnumeration
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.validity_parameter_assignment_version_structure import (
    ValidityParameterAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GenericParameterAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FARE ACCESS RIGHT PARAMETERs.
    """

    class Meta:
        name = "genericParameterAssignments_RelStructure"

    generic_parameter_assignment_or_generic_parameter_assignment_in_context: List[
        Union[
            "GenericParameterAssignment", "GenericParameterAssignmentInContext"
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GenericParameterAssignment",
                    "type": ForwardRef("GenericParameterAssignment"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": ForwardRef("GenericParameterAssignmentInContext"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class GenericParameterAssignmentVersionStructure(
    ValidityParameterAssignmentVersionStructure
):
    """
    Type for Generic PARAMETER ASSIGNMENT.

    :ivar includes_grouping_type: Operator for Grouping Scope Elements.
        Default is OR.
    :ivar includes: Assignments Logically included in this group. Groups
        are combined acording to the Operator.
    """

    class Meta:
        name = "GenericParameterAssignment_VersionStructure"

    includes_grouping_type: Optional[BooleanOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "IncludesGroupingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    includes: Optional[GenericParameterAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class GenericParameterAssignment(GenericParameterAssignmentVersionStructure):
    """
    A VALIDITY PARAMETER ASSIGNMENT specifying practical parameters during a TRAVEL
    GenericATION, within a given fare structure (e.g. the origin or destination
    zone in a zone-counting system).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GenericParameterAssignmentInContext(
    GenericParameterAssignmentVersionStructure
):
    """Optimisation: Can be used without id constraintA VALIDITY PARAMETER ASSIGNMENT specifying practical parameters during a TRAVEL GenericATION, within a given fare structure (e.g. the origin or destination zone in a zone-counting system)."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
