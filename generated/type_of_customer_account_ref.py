from dataclasses import dataclass

from generated.type_of_customer_account_ref_structure import (
    TypeOfCustomerAccountRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfCustomerAccountRef(TypeOfCustomerAccountRefStructure):
    """
    Reference to a TYPE OF CUSTOMER ACCOUNT .
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
