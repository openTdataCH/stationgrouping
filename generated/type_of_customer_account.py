from dataclasses import dataclass

from generated.type_of_customer_account_version_structure import (
    TypeOfCustomerAccountVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfCustomerAccount(TypeOfCustomerAccountVersionStructure):
    """
    A classification of a CUSTOMER ACCOUNT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
