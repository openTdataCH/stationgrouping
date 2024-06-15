from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from generated.derived_view_structure import DerivedViewStructure
from generated.timing_link_in_journey_pattern_ref import (
    TimingLinkInJourneyPatternRef,
)
from generated.timing_link_ref import TimingLinkRef
from generated.timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnwardTimingLinkDerivedViewStructure(DerivedViewStructure):
    """
    Type for Information about onwards TIMING LINK.

    :ivar timing_link_in_journey_pattern_ref:
    :ivar timing_link_ref:
    :ivar to_point_ref: Identifier of POINT at which LINK ends.
    :ivar run_time: Run time for TIMING LINK - TIME BAND given by
        context.
    """

    class Meta:
        name = "OnwardTimingLink_DerivedViewStructure"

    timing_link_in_journey_pattern_ref: Optional[
        TimingLinkInJourneyPatternRef
    ] = field(
        default=None,
        metadata={
            "name": "TimingLinkInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_link_ref: Optional[TimingLinkRef] = field(
        default=None,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_point_ref: Optional[TimingPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    run_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
