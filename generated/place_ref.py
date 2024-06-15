from dataclasses import dataclass

from generated.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceRef(PlaceRefStructure):
    """
    Reference to a PLACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
