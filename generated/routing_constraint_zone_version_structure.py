from dataclasses import dataclass, field
from typing import Optional, Union

from generated.group_of_lines_ref import GroupOfLinesRef
from generated.line_refs_rel_structure import LineRefsRelStructure
from generated.network_ref import NetworkRef
from generated.points_in_journey_pattern_rel_structure import (
    PointsInJourneyPatternRelStructure,
)
from generated.zone_use_enumeration import ZoneUseEnumeration
from generated.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutingConstraintZoneVersionStructure(ZoneVersionStructure):
    """
    Type for ROUTING CONSTRAINT ZONE.

    :ivar zone_use: How Zone may be used.
    :ivar points_in_pattern: Points that constraint limits to, in
        sequence.
    :ivar lines: LINEs associated with ROUTING CONSTRAINT ZONE.
    :ivar network_ref_or_group_of_lines_ref:
    """

    class Meta:
        name = "RoutingConstraintZone_VersionStructure"

    zone_use: Optional[ZoneUseEnumeration] = field(
        default=None,
        metadata={
            "name": "ZoneUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    points_in_pattern: Optional[PointsInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsInPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lines: Optional[LineRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    network_ref_or_group_of_lines_ref: Optional[
        Union[NetworkRef, GroupOfLinesRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "NetworkRef",
                    "type": NetworkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinesRef",
                    "type": GroupOfLinesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
