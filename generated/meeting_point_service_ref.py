from dataclasses import dataclass

from generated.meeting_point_service_ref_structure import (
    MeetingPointServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MeetingPointServiceRef(MeetingPointServiceRefStructure):
    """
    Identifier of an MEETING POINT SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
