from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union

from generated.authority_ref import AuthorityRef
from generated.common_section_point_members_rel_structure import (
    CommonSectionPointMembersRelStructure,
)
from generated.common_section_ref import CommonSectionRef
from generated.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from generated.destination_display_ref import DestinationDisplayRef
from generated.destination_display_view import DestinationDisplayView
from generated.direction_ref import DirectionRef
from generated.direction_type_enumeration import DirectionTypeEnumeration
from generated.direction_view import DirectionView
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.fare_point_in_pattern_ref_structure import (
    FarePointInPatternRefStructure,
)
from generated.fare_section_ref import FareSectionRef
from generated.flexible_line_ref import FlexibleLineRef
from generated.general_section_ref import GeneralSectionRef
from generated.info_links_rel_structure import InfoLinksRelStructure
from generated.journey_pattern_headways_rel_structure import (
    JourneyPatternHeadwaysRelStructure,
)
from generated.journey_pattern_layovers_rel_structure import (
    JourneyPatternLayoversRelStructure,
)
from generated.journey_pattern_ref import JourneyPatternRef
from generated.journey_pattern_run_times_rel_structure import (
    JourneyPatternRunTimesRelStructure,
)
from generated.journey_pattern_wait_times_rel_structure import (
    JourneyPatternWaitTimesRelStructure,
)
from generated.line_ref import LineRef
from generated.line_section_ref import LineSectionRef
from generated.link_in_link_sequence_versioned_child_structure import (
    LinkInLinkSequenceVersionedChildStructure,
)
from generated.link_sequence_refs_rel_structure import (
    LinkSequenceRefsRelStructure,
)
from generated.links_in_journey_pattern_rel_structure import (
    LinksInJourneyPatternRelStructure,
)
from generated.links_on_section_rel_structure import LinksOnSectionRelStructure
from generated.multilingual_string import MultilingualString
from generated.notice_assignments_rel_structure import (
    NoticeAssignmentsRelStructure,
)
from generated.operational_context_ref import OperationalContextRef
from generated.operator_ref import OperatorRef
from generated.parent_common_section_ref import ParentCommonSectionRef
from generated.point_on_line_sections_rel_structure import (
    PointOnLineSectionsRelStructure,
)
from generated.points_in_journey_pattern_rel_structure import (
    PointsInJourneyPatternRelStructure,
)
from generated.points_on_section_rel_structure import (
    PointsOnSectionRelStructure,
)
from generated.private_code import PrivateCode
from generated.projections_rel_structure import ProjectionsRelStructure
from generated.purpose_of_grouping_ref import PurposeOfGroupingRef
from generated.route_ref import RouteRef
from generated.route_view import RouteView
from generated.section_ref import SectionRef
from generated.section_type_enumeration import SectionTypeEnumeration
from generated.service_journey_pattern_ref import ServiceJourneyPatternRef
from generated.service_pattern_ref import ServicePatternRef
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from generated.timing_pattern_ref import TimingPatternRef
from generated.type_of_journey_pattern_ref import TypeOfJourneyPatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SectionsInSequenceRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of  SECTIONS in sequence.

    :ivar section_in_sequence: A SECTION in SEQUENCE.
    """

    class Meta:
        name = "sectionsInSequence_RelStructure"

    section_in_sequence: List["SectionInSequence"] = field(
        default_factory=list,
        metadata={
            "name": "SectionInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class LinkSequenceVersionStructure(DataManagedObjectStructure):
    """
    Type for an Abstract LINK SEQUENCE.

    :ivar name: Name of LINK SEQUENCE.
    :ivar short_name: Short Name of LINK SEQUENCE.
    :ivar description: Further Description of a LINKSEQUENCE.
    :ivar distance: Overall distance of LINK SEQUENCE. Can be derived
        from component LINKs.
    :ivar private_code:
    :ivar projections: PROJECTIONs of LINK SEQUENCE onto another ENTITY
        or layer.
    :ivar info_links: Hyperlinks associated with JOURNEY.
    :ivar sections_in_sequence: SECTIONS that make up route.  Can be
        used as an alternative to  points in Seqnece. POINTS and LINKS
        must be of same type as sequence, eg ROUTE, ROUTE POINT, ROUTE
        LINK
    """

    class Meta:
        name = "LinkSequence_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    projections: Optional[ProjectionsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    info_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "infoLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sections_in_sequence: Optional[SectionsInSequenceRelStructure] = field(
        default=None,
        metadata={
            "name": "sectionsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class JourneyPatternVersionStructure(LinkSequenceVersionStructure):
    """
    Type for JOURNEY PATTERN.

    :ivar route_ref_or_route_view:
    :ivar direction_type: DIRECTION of JOURNEY PATTERN. Should be same
        as for ROUTE on which PATTERN is based.
    :ivar direction_ref_or_direction_view:
    :ivar destination_display_ref_or_destination_display_view:
    :ivar type_of_journey_pattern_ref:
    :ivar operational_context_ref:
    :ivar timing_pattern_ref: Reference to a TIMING PATTERN.
    :ivar notice_assignments: Notices for JOURNEY PATTERN Points may be
    :ivar run_times: Ordered run times for JOURNEY PATTERN, specific to
        a TIME DEMAND TYPE.
    :ivar wait_times: WAIT TIMEs for JOURNEY PATTERN, specific to a TIME
        DEMAND TYPE.
    :ivar headways: Wait times for TIMING POINT. There may be different
        times for different time demands.
    :ivar layovers: Layovers associated with JOURNEY PATTERN.
    :ivar points_in_sequence: Sequence of points in JOURNEY PATTERN
        Points may be SCHEDULED STOP POINTs or TIMING POINTs.
    :ivar links_in_sequence: Sequence of points in JOURNEY PATTERN
        Points may be SCHEDULED STOP POINTs or TIMING POINTs.
    """

    class Meta:
        name = "JourneyPattern_VersionStructure"

    route_ref_or_route_view: Optional[Union[RouteRef, RouteView]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RouteRef",
                    "type": RouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteView",
                    "type": RouteView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    direction_type: Optional[DirectionTypeEnumeration] = field(
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
    destination_display_ref_or_destination_display_view: Optional[
        Union[DestinationDisplayRef, DestinationDisplayView]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DestinationDisplayRef",
                    "type": DestinationDisplayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayView",
                    "type": DestinationDisplayView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_journey_pattern_ref: Optional[TypeOfJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "TypeOfJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_pattern_ref: Optional[TimingPatternRef] = field(
        default=None,
        metadata={
            "name": "TimingPatternRef",
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
    run_times: Optional[JourneyPatternRunTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wait_times: Optional[JourneyPatternWaitTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "waitTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    headways: Optional[JourneyPatternHeadwaysRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    layovers: Optional[JourneyPatternLayoversRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    points_in_sequence: Optional[PointsInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    links_in_sequence: Optional[LinksInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "linksInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class SectionVersionStructure(LinkSequenceVersionStructure):
    """Type for  SECTION.

    +v1.1.

    :ivar purpose_of_grouping_ref: Reference to a PURPOSE OF GROUPING.
    :ivar used_in: LINK SEQUENCES using SECTION.
    :ivar name_of_link_class: Name of Link Cass of COMMON SECTION
    """

    class Meta:
        name = "Section_VersionStructure"

    purpose_of_grouping_ref: Optional[PurposeOfGroupingRef] = field(
        default=None,
        metadata={
            "name": "PurposeOfGroupingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    used_in: Optional[LinkSequenceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "usedIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name_of_link_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfLinkClass",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CommonSectionVersionStructure(SectionVersionStructure):
    """
    Type for COMMON SECTION.
    """

    class Meta:
        name = "CommonSection_VersionStructure"

    points_on_section_or_members: Optional[
        Union[
            PointsOnSectionRelStructure, CommonSectionPointMembersRelStructure
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "pointsOnSection",
                    "type": PointsOnSectionRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "members",
                    "type": CommonSectionPointMembersRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class GeneralSectionVersionStructure(SectionVersionStructure):
    """Type for GENERAL SECTION.

    +v1.1.

    :ivar points_on_section: Ordered collection of POINTS used in the
        GENERAL SECTION.
    :ivar links_on_section: Ordered collection of LINKSused in the
        GENERAL SECTION.
    """

    class Meta:
        name = "GeneralSection_VersionStructure"

    points_on_section: Optional[PointsOnSectionRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    links_on_section: Optional[LinksOnSectionRelStructure] = field(
        default=None,
        metadata={
            "name": "linksOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class JourneyPattern(JourneyPatternVersionStructure):
    """An ordered list of SCHEDULED STOP POINTs and TIMING POINTs on a single
    ROUTE, describing the pattern of working for public transport vehicles.

    A JOURNEY PATTERN may pass through the same POINT more than once.
    The first point of a JOURNEY PATTERN is the origin. The last point
    is the destination.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineSectionVersionStructure(SectionVersionStructure):
    """
    Type for a LINE SECTION.

    :ivar points_on_section_or_members:
    :ivar reverse_points_on_section_or_reverse_members:
    :ivar section_type: Nature of LINE SECTION. Default is trunK.
    :ivar flexible_line_ref_or_line_ref:
    :ivar authority_ref_or_operator_ref:
    """

    class Meta:
        name = "LineSection_VersionStructure"

    points_on_section_or_members: Optional[
        Union[
            PointOnLineSectionsRelStructure,
            CommonSectionPointMembersRelStructure,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "pointsOnSection",
                    "type": PointOnLineSectionsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "members",
                    "type": CommonSectionPointMembersRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    reverse_points_on_section_or_reverse_members: Optional[
        Union[
            PointOnLineSectionsRelStructure,
            CommonSectionPointMembersRelStructure,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "reversePointsOnSection",
                    "type": PointOnLineSectionsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "reverseMembers",
                    "type": CommonSectionPointMembersRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    section_type: Optional[SectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "SectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_line_ref_or_line_ref: Optional[
        Union[FlexibleLineRef, LineRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    authority_ref_or_operator_ref: Optional[
        Union[AuthorityRef, OperatorRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class CommonSection(CommonSectionVersionStructure):
    """A shared set of LINKS or POINTs.

    A part of a public transport network where the ROUTEs of several
    JOURNEY PATTERNs are going in parallel and where the synchronisation
    of SERVICE JOURNEYs may be planned and controlled with respect to
    commonly used LINKs and STOP POINTs. COMMON SECTIONs are defined
    arbitrarily and need not cover the total lengths of topologically
    bundled sections.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareSectionVersionStructure(GeneralSectionVersionStructure):
    """
    Type for FARE SECTION.

    :ivar choice:
    :ivar from_point_in_pattern_ref: FARE POINT IN JOURNEY PATTERN at
        which FARE SECTION begins.
    :ivar to_point_in_pattern_ref: FARE POINT IN JOURNEY PATTERN at
        which FARE SECTION ends.
    """

    class Meta:
        name = "FareSection_VersionStructure"

    choice: Optional[
        Union[
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
            JourneyPattern,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
                    "name": "JourneyPattern",
                    "type": JourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    from_point_in_pattern_ref: Optional[FarePointInPatternRefStructure] = (
        field(
            default=None,
            metadata={
                "name": "FromPointInPatternRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    to_point_in_pattern_ref: Optional[FarePointInPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "ToPointInPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class GeneralSection(GeneralSectionVersionStructure):
    """A  resuable sequence of LINKS or POINTs.

    +v1.1.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineSection(LineSectionVersionStructure):
    """A section of a LINE NETWORK comprising an edge between two nodes.

    Not directional.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareSection(FareSectionVersionStructure):
    """
    A subdivision of a JOURNEY PATTERN consisting of consecutive POINTs IN JOURNEY
    PATTERN, used to define an element of the fare structure.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SectionInSequenceVersionedChildStructure(
    LinkInLinkSequenceVersionedChildStructure
):
    """
    Type for a SECTION IN SEQUENCE.
    """

    class Meta:
        name = "SectionInSequence_VersionedChildStructure"

    choice_1: Optional[
        Union[
            ParentCommonSectionRef,
            CommonSectionRef,
            LineSectionRef,
            FareSectionRef,
            GeneralSectionRef,
            SectionRef,
            FareSection,
            CommonSection,
            LineSection,
            GeneralSection,
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
                {
                    "name": "FareSection",
                    "type": FareSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommonSection",
                    "type": CommonSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineSection",
                    "type": LineSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSection",
                    "type": GeneralSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SectionInSequence(SectionInSequenceVersionedChildStructure):
    """
    A SECTION in Sequence.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
