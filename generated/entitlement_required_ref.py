from dataclasses import dataclass

from generated.entitlement_required_ref_structure import (
    EntitlementRequiredRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementRequiredRef(EntitlementRequiredRefStructure):
    """
    Reference to a ENTITLEMENT REQUIRED PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
