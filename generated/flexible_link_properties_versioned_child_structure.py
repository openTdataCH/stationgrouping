from dataclasses import dataclass, field
from typing import Optional, Union

from generated.activation_link_ref import ActivationLinkRef
from generated.entity_in_version_structure import VersionedChildStructure
from generated.flexible_link_type_enumeration import (
    FlexibleLinkTypeEnumeration,
)
from generated.line_link_ref import LineLinkRef
from generated.path_link_ref import PathLinkRef
from generated.railway_link_ref import RailwayLinkRef
from generated.road_link_ref import RoadLinkRef
from generated.route_link_ref import RouteLinkRef
from generated.service_link_ref import ServiceLinkRef
from generated.timing_link_ref import TimingLinkRef
from generated.wire_link_ref import WireLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleLinkPropertiesVersionedChildStructure(VersionedChildStructure):
    """
    Type for FLEXIBLE LINK PROPERTies.

    :ivar choice:
    :ivar may_be_skipped: Whether the LINK may be skipped.
    :ivar on_main_route: Whether the LINK is on the main ROUTE of the
        LINE.
    :ivar unscheduled_path: Whether this link is on an unscheduled path
        route.
    :ivar flexible_link_type: Type of flexible link.
    """

    class Meta:
        name = "FlexibleLinkProperties_VersionedChildStructure"

    choice: Optional[
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
            ),
        },
    )
    may_be_skipped: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MayBeSkipped",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    on_main_route: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnMainRoute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    unscheduled_path: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnscheduledPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_link_type: Optional[FlexibleLinkTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FlexibleLinkType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
