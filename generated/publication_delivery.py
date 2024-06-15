from dataclasses import dataclass

from generated.publication_delivery_structure import (
    PublicationDeliveryStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PublicationDelivery(PublicationDeliveryStructure):
    """A set of NeTEx objects as assembled by a publication request or other
    service.

    Provides a general purpose wrapper for NeTEx data content.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
