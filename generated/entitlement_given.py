from dataclasses import dataclass

from generated.entitlement_given_version_structure import (
    EntitlementGivenVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementGiven(EntitlementGivenVersionStructure):
    """
    A right to a SERVICE ACCESS RIGHT is given by a FARE  PRODUCT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
