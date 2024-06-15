from dataclasses import dataclass, field
from typing import List, Union

from generated.common_section_point_member import CommonSectionPointMember
from generated.line_section_point_member import LineSectionPointMember
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommonSectionPointMembersRelStructure(
    StrictContainmentAggregationStructure
):
    """DEPRECATED - Type for a list of COMMON SECTION POINT MEMBERs."""

    class Meta:
        name = "commonSectionPointMembers_RelStructure"

    line_section_point_member_or_common_section_point_member: List[
        Union[LineSectionPointMember, CommonSectionPointMember]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LineSectionPointMember",
                    "type": LineSectionPointMember,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommonSectionPointMember",
                    "type": CommonSectionPointMember,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
