from dataclasses import dataclass

from generated.customer_account_status_version_structure import (
    CustomerAccountStatusVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountStatus(CustomerAccountStatusVersionStructure):
    """
    A classification of a CUSTOMER ACCOUNT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
