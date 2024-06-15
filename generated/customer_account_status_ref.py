from dataclasses import dataclass

from generated.customer_account_status_ref_structure import (
    CustomerAccountStatusRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountStatusRef(CustomerAccountStatusRefStructure):
    """
    Reference to a CUSTOMER ACCOUNT STATUS .
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
