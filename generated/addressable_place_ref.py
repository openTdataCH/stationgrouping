from dataclasses import dataclass

from generated.addressable_place_ref_structure import (
    AddressablePlaceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AddressablePlaceRef(AddressablePlaceRefStructure):
    """
    Reference to an ADDRESSED PLACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
