from dataclasses import dataclass

from generated.notice_assignment_ref_structure import (
    NoticeAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesNoticeAssignmentRefStructure(NoticeAssignmentRefStructure):
    """
    Type for Reference to a SALES NOTICE ASSIGNMENT.
    """
