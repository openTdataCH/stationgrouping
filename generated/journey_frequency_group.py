from dataclasses import dataclass

from generated.journey_frequency_group_version_structure import (
    JourneyFrequencyGroupVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyFrequencyGroup(JourneyFrequencyGroupVersionStructure):
    """A group of JOURNEYs defined in order to describe special behaviour like
    frequency based services or rhythmical services (runs all xxh10, xxh25 and
    xxh45...

    for example; this is especially useful for passenger information).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
