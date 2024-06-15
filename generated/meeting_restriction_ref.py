from dataclasses import dataclass

from generated.meeting_restriction_ref_structure import (
    MeetingRestrictionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MeetingRestrictionRef(MeetingRestrictionRefStructure):
    """
    Reference to a MEETING RESTRICTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
