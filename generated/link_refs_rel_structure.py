from dataclasses import dataclass, field
from typing import List, Union

from generated.activation_link_ref import ActivationLinkRef
from generated.activation_link_ref_by_value import ActivationLinkRefByValue
from generated.line_link_ref import LineLinkRef
from generated.line_link_ref_by_value import LineLinkRefByValue
from generated.link_ref_by_value import LinkRefByValue
from generated.modal_link_ref_by_value import ModalLinkRefByValue
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.path_link_ref import PathLinkRef
from generated.path_link_ref_by_value import PathLinkRefByValue
from generated.railway_link_ref import RailwayLinkRef
from generated.railway_link_ref_by_value import RailwayLinkRefByValue
from generated.road_link_ref import RoadLinkRef
from generated.road_link_ref_by_value import RoadLinkRefByValue
from generated.route_link_ref import RouteLinkRef
from generated.route_link_ref_by_value import RouteLinkRefByValue
from generated.service_link_ref import ServiceLinkRef
from generated.service_link_ref_by_value import ServiceLinkRefByValue
from generated.timing_link_ref import TimingLinkRef
from generated.timing_link_ref_by_value import TimingLinkRefByValue
from generated.wire_link_ref import WireLinkRef
from generated.wire_link_ref_by_value import WireLinkRefByValue

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a LINK.
    """

    class Meta:
        name = "linkRefs_RelStructure"

    choice: List[
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
            ServiceLinkRefByValue,
            LineLinkRefByValue,
            PathLinkRefByValue,
            TimingLinkRefByValue,
            RouteLinkRefByValue,
            WireLinkRefByValue,
            RoadLinkRefByValue,
            RailwayLinkRefByValue,
            ActivationLinkRefByValue,
            ModalLinkRefByValue,
            LinkRefByValue,
        ]
    ] = field(
        default_factory=list,
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
                    "name": "ServiceLinkRefByValue",
                    "type": ServiceLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineLinkRefByValue",
                    "type": LineLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkRefByValue",
                    "type": PathLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkRefByValue",
                    "type": TimingLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteLinkRefByValue",
                    "type": RouteLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireLinkRefByValue",
                    "type": WireLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadLinkRefByValue",
                    "type": RoadLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayLinkRefByValue",
                    "type": RailwayLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationLinkRefByValue",
                    "type": ActivationLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ModalLinkRefByValue",
                    "type": ModalLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkRefByValue",
                    "type": LinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
