from dataclasses import dataclass

from generated.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleQuayRefStructure(PlaceRefStructure):
    """
    Type for reference to a FLEXIBLE QUAY.
    """
