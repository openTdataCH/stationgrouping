from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.notice_assignment import NoticeAssignment
from generated.sales_notice_assignment import SalesNoticeAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticeAssignmentsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of NOTICE ASSIGNMENTs.
    """

    class Meta:
        name = "noticeAssignmentsInFrame_RelStructure"

    sales_notice_assignment_or_notice_assignment: List[
        Union[SalesNoticeAssignment, NoticeAssignment]
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
            ),
        },
    )
