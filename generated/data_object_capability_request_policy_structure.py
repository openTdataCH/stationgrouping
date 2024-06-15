from dataclasses import dataclass

from generated.capability_request_policy_structure import (
    CapabilityRequestPolicyStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectCapabilityRequestPolicyStructure(
    CapabilityRequestPolicyStructure
):
    """
    Type for Monitoring Service Capability Request Policy.
    """
