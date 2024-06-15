from dataclasses import dataclass

from generated.journey_timing_ref_structure import JourneyTimingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyTimingRef(JourneyTimingRefStructure):
    """
    Reference to a JOURNEY TIMING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
