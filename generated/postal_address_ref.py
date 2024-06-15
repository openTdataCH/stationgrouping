from dataclasses import dataclass

from generated.postal_address_ref_structure import PostalAddressRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PostalAddressRef(PostalAddressRefStructure):
    """
    Reference to a POSTAL ADDRESS.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
