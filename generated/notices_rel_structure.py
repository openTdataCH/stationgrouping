from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.notice import Notice
from generated.notice_ref import NoticeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of NOTICEs.
    """

    class Meta:
        name = "notices_RelStructure"

    notice_ref_or_notice: List[Union[NoticeRef, Notice]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "NoticeRef",
                    "type": NoticeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Notice",
                    "type": Notice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
