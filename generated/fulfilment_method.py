from dataclasses import dataclass

from generated.fulfilment_method_version_structure import (
    FulfilmentMethodVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FulfilmentMethod(FulfilmentMethodVersionStructure):
    """The means by which the ticket is delivered to the Customer.

    e.g. online, collection, etc.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
