from dataclasses import dataclass

from generated.journey_meeting_derived_view_structure import (
    JourneyMeetingDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyMeetingView(JourneyMeetingDerivedViewStructure):
    """
    Simplified  view of JOURNEY MEETING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
