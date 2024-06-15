from dataclasses import dataclass

from generated.meeting_restriction_version_structure import (
    MeetingRestrictionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MeetingRestriction(MeetingRestrictionVersionStructure):
    """
    A pair of INFRASTRUCTURE LINKs where vehicles of specified VEHICLE TYPEs are
    not allowed to meet.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
