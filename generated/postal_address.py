from dataclasses import dataclass

from generated.postal_address_version_structure import (
    PostalAddressVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PostalAddress(PostalAddressVersionStructure):
    """
    A POSTAL ADDRESS to which mail can be sent.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
