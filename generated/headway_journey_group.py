from dataclasses import dataclass

from generated.headway_journey_group_version_structure import (
    HeadwayJourneyGroupVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HeadwayJourneyGroup(HeadwayJourneyGroupVersionStructure):
    """A group of VEHICLE JOURNEYs following the same JOURNEY PATTERN and having
    the same headway interval between a specified start and end time (for example,
    ‘every 10 minutes’).

    This is especially useful for presenting passenger information.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
