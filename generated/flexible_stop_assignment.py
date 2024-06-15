from dataclasses import dataclass

from generated.flexible_stop_assignment_version_structure import (
    FlexibleStopAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleStopAssignment(FlexibleStopAssignmentVersionStructure):
    """Assignment of a SCHEDULED STOP POINT to a FLEXIBLE STOP PLACE and quay.

    etc.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
