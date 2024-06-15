from dataclasses import dataclass

from generated.notice_assignment_version_structure import (
    NoticeAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticeAssignment(NoticeAssignmentVersionStructure):
    """
    The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON
    SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY
    PATTERN the validity of the NOTICE starts and ends respectively.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
