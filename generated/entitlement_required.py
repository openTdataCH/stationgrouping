from dataclasses import dataclass

from generated.entitlement_required_version_structure import (
    EntitlementRequiredVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementRequired(EntitlementRequiredVersionStructure):
    """
    A rerirement to a SERVICE ACCESS RIGHT in order to purchase or use PRODUCT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
