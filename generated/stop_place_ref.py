from dataclasses import dataclass

from generated.stop_place_ref_structure import StopPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceRef(StopPlaceRefStructure):
    """
    Reference to a STOP PLACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
