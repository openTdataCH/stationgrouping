from dataclasses import dataclass, field
from typing import Optional, Union

from generated.activation_link_ref import ActivationLinkRef
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.line_link_ref import LineLinkRef
from generated.multilingual_string import MultilingualString
from generated.path_link_ref import PathLinkRef
from generated.railway_link_ref import RailwayLinkRef
from generated.road_link_ref import RoadLinkRef
from generated.route_link_ref import RouteLinkRef
from generated.service_link_ref import ServiceLinkRef
from generated.timing_link_ref import TimingLinkRef
from generated.wire_link_ref import WireLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineShapeStructure2(DataManagedObjectStructure):
    """
    Type for a LINE SHAPE.

    :ivar formula: Formula for calculating line.
    :ivar name: Name of LINE SHAPE.
    :ivar choice:
    :ivar locating_system_ref: Name of locating system under which line
        is specified.
    """

    class Meta:
        name = "LineShapeStructure"

    formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "Formula",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
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
    locating_system_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatingSystemRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
