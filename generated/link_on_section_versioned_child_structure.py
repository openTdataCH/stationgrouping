from dataclasses import dataclass, field
from typing import Optional, Union

from generated.activation_link import ActivationLink
from generated.activation_link_ref import ActivationLinkRef
from generated.line_link_ref import LineLinkRef
from generated.link_in_link_sequence_versioned_child_structure import (
    LinkInLinkSequenceVersionedChildStructure,
)
from generated.path_link import PathLink
from generated.path_link_ref import PathLinkRef
from generated.railway_element import RailwayElement
from generated.railway_link_ref import RailwayLinkRef
from generated.road_element import RoadElement
from generated.road_link_ref import RoadLinkRef
from generated.route_link import RouteLink
from generated.route_link_ref import RouteLinkRef
from generated.service_link import ServiceLink
from generated.service_link_ref import ServiceLinkRef
from generated.site_path_link import SitePathLink
from generated.timing_link import TimingLink
from generated.timing_link_ref import TimingLinkRef
from generated.wire_element import WireElement
from generated.wire_link_ref import WireLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkOnSectionVersionedChildStructure(
    LinkInLinkSequenceVersionedChildStructure
):
    """Type for a LINK on a SECTION.

    +v1.1.

    :ivar choice_1:
    :ivar reverse: Whether link is navigated in to / from, i.e. reverse
        direction . Default is false, i.e. from to.
    """

    class Meta:
        name = "LinkOnSection_VersionedChildStructure"

    choice_1: Optional[
        Union[
            ServiceLinkRef,
            LineLinkRef,
            PathLinkRef,
            TimingLinkRef,
            RouteLinkRef,
            WireLinkRef,
            RoadLinkRef,
            RailwayLinkRef,
            ActivationLinkRef,
            ServiceLink,
            SitePathLink,
            PathLink,
            RouteLink,
            TimingLink,
            WireElement,
            RoadElement,
            RailwayElement,
            ActivationLink,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceLinkRef",
                    "type": ServiceLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineLinkRef",
                    "type": LineLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkRef",
                    "type": PathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkRef",
                    "type": TimingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteLinkRef",
                    "type": RouteLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireLinkRef",
                    "type": WireLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadLinkRef",
                    "type": RoadLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayLinkRef",
                    "type": RailwayLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationLinkRef",
                    "type": ActivationLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceLink",
                    "type": ServiceLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathLink",
                    "type": SitePathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLink",
                    "type": PathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteLink",
                    "type": RouteLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLink",
                    "type": TimingLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireElement",
                    "type": WireElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadElement",
                    "type": RoadElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayElement",
                    "type": RailwayElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationLink",
                    "type": ActivationLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    reverse: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reverse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
