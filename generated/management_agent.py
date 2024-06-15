from dataclasses import dataclass

from generated.management_agent_version_structure import (
    ManagementAgentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ManagementAgent(ManagementAgentVersionStructure):
    """
    ORGANISATION that manages data or a SITE or FACILITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
