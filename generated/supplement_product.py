from dataclasses import dataclass

from generated.supplement_product_version_structure import (
    SupplementProductVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SupplementProduct(SupplementProductVersionStructure):
    """
    A FARE PRODUCT consisting of one or several VALIDABLE ELEMENTs, specific to a
    CHARGING MOMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
