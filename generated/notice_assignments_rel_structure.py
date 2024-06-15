from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.notice_assignment import NoticeAssignment
from generated.notice_assignment_view import NoticeAssignmentView
from generated.sales_notice_assignment import SalesNoticeAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticeAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of NOTICE ASSIGNMENTs.
    """

    class Meta:
        name = "noticeAssignments_RelStructure"

    sales_notice_assignment_or_notice_assignment_or_notice_assignment_view: List[
        Union[SalesNoticeAssignment, NoticeAssignment, NoticeAssignmentView]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesNoticeAssignment",
                    "type": SalesNoticeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NoticeAssignment",
                    "type": NoticeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NoticeAssignmentView",
                    "type": NoticeAssignmentView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
