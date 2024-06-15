from dataclasses import dataclass, field
from typing import Optional, Union

from generated.link_in_link_sequence_versioned_child_structure import (
    LinkInLinkSequenceVersionedChildStructure,
)
from generated.service_link_ref import ServiceLinkRef
from generated.timing_link_ref import TimingLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkInJourneyPatternVersionedChildStructure(
    LinkInLinkSequenceVersionedChildStructure
):
    """
    Type for LINK IN JOURNEY PATTERN.
    """

    class Meta:
        name = "LinkInJourneyPattern_VersionedChildStructure"

    service_link_ref_or_timing_link_ref: Optional[
        Union[ServiceLinkRef, TimingLinkRef]
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
                    "name": "TimingLinkRef",
                    "type": TimingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
