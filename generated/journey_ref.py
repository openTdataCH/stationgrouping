from dataclasses import dataclass

from generated.journey_ref_structure import JourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyRef(JourneyRefStructure):
    """
    Reference to a JOURNEY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
