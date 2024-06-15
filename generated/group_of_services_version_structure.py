from dataclasses import dataclass, field
from typing import List, Optional, Union

from generated.day_type_ref_structure import DayTypeRefStructure
from generated.destination_display_refs_rel_structure import (
    DestinationDisplayRefsRelStructure,
)
from generated.direction_ref import DirectionRef
from generated.direction_type import DirectionType
from generated.direction_view import DirectionView
from generated.group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from generated.group_of_services_end_point_derived_view_structure import (
    GroupOfServicesEndPointDerivedViewStructure,
)
from generated.group_of_services_members_rel_structure import (
    GroupOfServicesMembersRelStructure,
)
from generated.notice_assignments_rel_structure import (
    NoticeAssignmentsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfServicesVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for a GROUP OF SERVICEs.

    :ivar day_types: The DAY TYPEs of all the services in this group.
    :ivar direction_type:
    :ivar direction_ref_or_direction_view:
    :ivar origin: Origin associated with this GROUP OF SERVICEs.
    :ivar destination: Destination associated with this GROUP OF
        SERVICEs.
    :ivar destination_displays: Destinations associated with this GROUP
        OF SERVICEs, including via points.
    :ivar members: Services in GROUP.
    :ivar notice_assignments: NOTICEs  relevant for the whole GROUP OF
        SERVICEs.
    """

    class Meta:
        name = "GroupOfServices_VersionStructure"

    day_types: Optional["GroupOfServicesVersionStructure.DayTypes"] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_type: Optional[DirectionType] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_ref_or_direction_view: Optional[
        Union[DirectionRef, DirectionView]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DirectionRef",
                    "type": DirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DirectionView",
                    "type": DirectionView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    origin: Optional[GroupOfServicesEndPointDerivedViewStructure] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination: Optional[GroupOfServicesEndPointDerivedViewStructure] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_displays: Optional[DestinationDisplayRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "destinationDisplays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: Optional[GroupOfServicesMembersRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class DayTypes:
        """
        :ivar day_type_ref: The DAY TYPE of all the services in this
            group.
        """

        day_type_ref: List[DayTypeRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "DayTypeRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
