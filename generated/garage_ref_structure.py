from dataclasses import dataclass

from generated.addressable_place_ref_structure import (
    AddressablePlaceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GarageRefStructure(AddressablePlaceRefStructure):
    """
    Type for a reference to a GARAGE.
    """
