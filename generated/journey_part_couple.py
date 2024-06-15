from dataclasses import dataclass

from generated.journey_part_couple_version_structure import (
    JourneyPartCoupleVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPartCouple(JourneyPartCoupleVersionStructure):
    """
    Two or more  JOURNEY PARTs of different VEHICLE JOURNEYs served simultaneously
    by a train set up by coupling their single vehicles.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
