from dataclasses import dataclass

from generated.address_ref_structure import AddressRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AddressRef(AddressRefStructure):
    """
    Reference to an ADDRESS.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
