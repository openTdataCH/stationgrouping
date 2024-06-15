from dataclasses import dataclass

from generated.headway_journey_group_ref_structure import (
    HeadwayJourneyGroupRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HeadwayJourneyGroupRef(HeadwayJourneyGroupRefStructure):
    """
    Reference to a HEADWAY JOURNEY GROUP.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
