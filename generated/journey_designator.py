from dataclasses import dataclass

from generated.journey_designator_structure import JourneyDesignatorStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyDesignator(JourneyDesignatorStructure):
    """Value reference to a JOURNEY.

    Provides an alternative way of identifying a Journey between TIMING
    POINTS
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
