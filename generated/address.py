from dataclasses import dataclass

from generated.address_version_structure import AddressVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Address(AddressVersionStructure):
    """
    An ADDRESS.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
