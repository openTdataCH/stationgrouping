from dataclasses import dataclass

from generated.journey_part_couple_ref_structure import (
    JourneyPartCoupleRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPartCoupleRef(JourneyPartCoupleRefStructure):
    """
    Reference to a JOURNEY PART COUPLE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
