from dataclasses import dataclass

from generated.distribution_assignment_version_structure import (
    DistributionAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistributionAssignment(DistributionAssignmentVersionStructure):
    """
    An assignment  of the  COUNTRY and/or  DISTRIBUTION CHANNEL through which a
    product may or may not be distributed.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
