from dataclasses import dataclass

from generated.charging_policy_ref_structure import ChargingPolicyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingPolicyRef(ChargingPolicyRefStructure):
    """
    Reference to a CHARGING POLICY usage parameter.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
