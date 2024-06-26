from dataclasses import dataclass

from generated.journey_meeting_ref_structure import JourneyMeetingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyMeetingRef(JourneyMeetingRefStructure):
    """
    Reference to a JOURNEY MEETING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
