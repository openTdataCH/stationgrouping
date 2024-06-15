from dataclasses import dataclass, field
from typing import Any

from generated.customer_purchase_package_element_access_versioned_child_structure import (
    CustomerPurchasePackageElementAccessVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackageElementAccess(
    CustomerPurchasePackageElementAccessVersionedChildStructure
):
    """Access to a VALIDABLE ELEMENT by a specific CUSTOMER PURCHASE PACKAGE
    through use of CUSTOMER PURCHASE PACKAGE.

    This is needed for validation of complex SALES OFFER PACKAGEs
    containing tariffs structures that have FARE STRUCTURE ELEMENTs IN
    SEQUENCE, in such a case a given SALES PACKAGE ELEMENT may have
    multiple VALIDABLE ELEMENTs associated with it, each of which can be
    separately validated and marked. +v1.1

    :ivar validity_conditions_or_valid_between:
    :ivar alternative_texts: Additional Translations of text  elements.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
