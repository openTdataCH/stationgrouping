from dataclasses import dataclass

from generated.management_agent_ref_structure import (
    ManagementAgentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ManagementAgentRef(ManagementAgentRefStructure):
    """
    Reference to a MANAGEMENT AGENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
