from dataclasses import dataclass

from generated.relief_opportunity_ref_structure import (
    ReliefOpportunityRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefOpportunityRef(ReliefOpportunityRefStructure):
    """
    Reference to a RELIEF OPPORTUNITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
