from dataclasses import dataclass

from generated.customer_version_structure import CustomerVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Customer(CustomerVersionStructure):
    """An identified person or organisation involved in a fare process.

    There may be a FARE CONTRACT between the CUSTOMER and the OPERATOR
    or the AUTHORITY ruling the consumption of services.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
