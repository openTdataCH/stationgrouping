from dataclasses import dataclass, field
from typing import Optional, Union

from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.flexible_line_ref import FlexibleLineRef
from generated.group_of_lines_ref import GroupOfLinesRef
from generated.line_ref import LineRef
from generated.line_sections_rel_structure import LineSectionsRelStructure
from generated.multilingual_string import MultilingualString
from generated.network_ref import NetworkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineNetworkVersionStructure(DataManagedObjectStructure):
    """
    Type for a LINE NETWORK restricts id.

    :ivar name: Name of LINE NETWORK.
    :ivar description: Description of LINE NETWORK.
    :ivar network_ref_or_group_of_lines_ref:
    :ivar flexible_line_ref_or_line_ref:
    :ivar sections: LINE SECTIONS within the LINE NETWORK.
    """

    class Meta:
        name = "LineNetwork_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
    sections: Optional[LineSectionsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
