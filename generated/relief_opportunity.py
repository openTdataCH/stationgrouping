from dataclasses import dataclass

from generated.relief_opportunity_version_structure import (
    ReliefOpportunityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefOpportunity(ReliefOpportunityVersionStructure):
    """A time in a BLOCK where a vehicle passes a RELIEF POINT.

    This opportunity may or may not be actually used for a relief.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
