from dataclasses import dataclass

from generated.penalty_policy_version_structure import (
    PenaltyPolicyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PenaltyPolicy(PenaltyPolicyVersionStructure):
    """
    Policy regarding different aspects of penalty charges, for example  repeated
    entry at the same station, no ticket etc.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
