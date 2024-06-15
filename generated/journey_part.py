from dataclasses import dataclass

from generated.journey_part_version_structure import (
    JourneyPartVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPart(JourneyPartVersionStructure):
    """
    A part of a VEHICLE JOURNEY created according to a specific functional purpose,
    for instance in situations when vehicle coupling or separating occurs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
