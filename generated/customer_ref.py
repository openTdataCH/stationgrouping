from dataclasses import dataclass

from generated.customer_ref_structure import CustomerRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerRef(CustomerRefStructure):
    """
    Reference to a CUSTOMER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
