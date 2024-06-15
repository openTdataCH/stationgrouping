from dataclasses import dataclass, field
from typing import Optional, Union

from generated.assignment_version_structure_1 import (
    AssignmentVersionStructure1,
)
from generated.common_section_ref import CommonSectionRef
from generated.dated_special_service_ref import DatedSpecialServiceRef
from generated.dated_vehicle_journey_ref import DatedVehicleJourneyRef
from generated.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from generated.dead_run_ref import DeadRunRef
from generated.fare_section_ref import FareSectionRef
from generated.general_group_of_entities_ref_structure import (
    GeneralGroupOfEntitiesRefStructure,
)
from generated.general_section_ref import GeneralSectionRef
from generated.journey_pattern_ref import JourneyPatternRef
from generated.line_section_ref import LineSectionRef
from generated.link_sequence_ref import LinkSequenceRef
from generated.navigation_path_ref import NavigationPathRef
from generated.notice import Notice
from generated.notice_ref import NoticeRef
from generated.parent_common_section_ref import ParentCommonSectionRef
from generated.point_in_sequence_ref_structure import (
    PointInSequenceRefStructure,
)
from generated.publicity_channel_enumeration import PublicityChannelEnumeration
from generated.route_ref import RouteRef
from generated.section_ref import SectionRef
from generated.service_journey_pattern_ref import ServiceJourneyPatternRef
from generated.service_journey_ref import ServiceJourneyRef
from generated.service_pattern_ref import ServicePatternRef
from generated.special_service_ref import SpecialServiceRef
from generated.template_service_journey_ref import TemplateServiceJourneyRef
from generated.timing_pattern_ref import TimingPatternRef
from generated.vehicle_journey_ref import VehicleJourneyRef
from generated.version_of_object_ref_structure import (
    VersionOfObjectRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticeAssignmentVersionStructure(AssignmentVersionStructure1):
    """
    Type for NOTICE ASSIGNMENT.

    :ivar notice_ref_or_group_of_notices_ref_or_notice:
    :ivar noticed_object_ref: Object with which NOTICE is associated. If
        given by context can be omitted.
    :ivar choice:
    :ivar choice_1:
    :ivar start_point_in_pattern_ref: POINT at which applicability of
        NOTICE starts.
    :ivar end_point_in_pattern_ref: POINT at which applicabiity of
        NOTICE endsIf absent same as Start Point.
    :ivar mark: Mark associated with NOTICE.
    :ivar mark_url: URL for image associated with NOTICE.
    :ivar publicity_channel: How NOTICE is to be publicised. Default is
        all.
    :ivar advertised: Whether NOTICE is advertised to public.
    """

    class Meta:
        name = "NoticeAssignment_VersionStructure"

    notice_ref_or_group_of_notices_ref_or_notice: Optional[
        Union[NoticeRef, GeneralGroupOfEntitiesRefStructure, Notice]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "NoticeRef",
                    "type": NoticeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfNoticesRef",
                    "type": GeneralGroupOfEntitiesRefStructure,
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
    noticed_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "NoticedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            DatedVehicleJourneyRef,
            DatedSpecialServiceRef,
            SpecialServiceRef,
            TemplateServiceJourneyRef,
            ServiceJourneyRef,
            DeadRunRef,
            VehicleJourneyRef,
            NavigationPathRef,
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
            TimingPatternRef,
            RouteRef,
            LinkSequenceRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DatedVehicleJourneyRef",
                    "type": DatedVehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedSpecialServiceRef",
                    "type": DatedSpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialServiceRef",
                    "type": SpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPathRef",
                    "type": NavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPatternRef",
                    "type": TimingPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteRef",
                    "type": RouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceRef",
                    "type": LinkSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice_1: Optional[
        Union[
            ParentCommonSectionRef,
            CommonSectionRef,
            LineSectionRef,
            FareSectionRef,
            GeneralSectionRef,
            SectionRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParentCommonSectionRef",
                    "type": ParentCommonSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommonSectionRef",
                    "type": CommonSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineSectionRef",
                    "type": LineSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareSectionRef",
                    "type": FareSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSectionRef",
                    "type": GeneralSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SectionRef",
                    "type": SectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    start_point_in_pattern_ref: Optional[PointInSequenceRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointInPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_point_in_pattern_ref: Optional[PointInSequenceRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointInPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mark",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mark_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "MarkUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    publicity_channel: Optional[PublicityChannelEnumeration] = field(
        default=None,
        metadata={
            "name": "PublicityChannel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    advertised: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Advertised",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
