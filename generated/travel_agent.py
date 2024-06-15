from dataclasses import dataclass

from generated.travel_agent_version_structure import (
    TravelAgentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelAgent(TravelAgentVersionStructure):
    """
    A travel agent who can retail travel products.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
