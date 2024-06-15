from dataclasses import dataclass

from generated.journey_version_structure import JourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Journey1(JourneyVersionStructure):
    """
    Common properties of a JOURNEY.
    """

    class Meta:
        name = "Journey"
        namespace = "http://www.netex.org.uk/netex"
