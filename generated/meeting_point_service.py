from dataclasses import dataclass

from generated.meeting_point_service_version_structure import (
    MeetingPointServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MeetingPointService(MeetingPointServiceVersionStructure):
    """
    Specialisation of CUSTOMER SERVICE for meeting points (provides characteristics
    like description, label, etc.).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
