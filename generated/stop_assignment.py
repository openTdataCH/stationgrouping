from dataclasses import dataclass

from generated.stop_assignment_version_structure import (
    StopAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopAssignment(StopAssignmentVersionStructure):
    """
    Assignment of a SCHEDULED STOP POINT to a STOP PLACE and QUAY, etc.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
