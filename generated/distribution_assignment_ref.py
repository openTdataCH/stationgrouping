from dataclasses import dataclass

from generated.distribution_assignment_ref_structure import (
    DistributionAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistributionAssignmentRef(DistributionAssignmentRefStructure):
    """
    Reference to a DISTRIBUTION ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
