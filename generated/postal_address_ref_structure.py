from dataclasses import dataclass

from generated.address_ref_structure import AddressRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PostalAddressRefStructure(AddressRefStructure):
    """
    Type for a reference to a TYPE OF ACTIVATION.
    """
