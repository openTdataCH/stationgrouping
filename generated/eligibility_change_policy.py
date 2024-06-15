from dataclasses import dataclass

from generated.eligibility_change_policy_version_structure import (
    EligibilityChangePolicyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EligibilityChangePolicy(EligibilityChangePolicyVersionStructure):
    """
    The policy to apply  if ta user's eligibility as a USER PROFILE changes.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
