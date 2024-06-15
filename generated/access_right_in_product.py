from dataclasses import dataclass

from generated.access_right_in_product_versioned_child_structure import (
    AccessRightInProductVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessRightInProduct(AccessRightInProductVersionedChildStructure):
    """
    A VALIDABLE ELEMENT as a part of a PRE-ASSIGNED FARE PRODUCT, including its
    possible order in the set of all VALIDABLE ELEMENTs grouped together to define
    the access right assigned to that PRE-ASSIGNED FARE PRODUCT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
