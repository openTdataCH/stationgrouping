from dataclasses import dataclass

from generated.addressable_place_version_structure import (
    AddressablePlaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AddressablePlace(AddressablePlaceVersionStructure):
    """
    A PLACE which may have an address.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
