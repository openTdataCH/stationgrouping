from dataclasses import dataclass

from generated.entitlement_given_ref_structure import (
    EntitlementGivenRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementGivenRef(EntitlementGivenRefStructure):
    """
    Reference to a ENTITLEMENT GIVEN PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
