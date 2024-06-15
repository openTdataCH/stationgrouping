from dataclasses import dataclass

from generated.customer_account_ref_structure import (
    CustomerAccountRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountRef(CustomerAccountRefStructure):
    """
    Reference to a CUSTOMER ACCOUNT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
