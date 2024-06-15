from dataclasses import dataclass

from generated.entitlement_product_version_structure import (
    EntitlementProductVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementProduct(EntitlementProductVersionStructure):
    """
    A precondition to access a service or to purchase a FARE PRODUCT issued by an
    organisation that may not be a PT operator (e.g. military card).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
