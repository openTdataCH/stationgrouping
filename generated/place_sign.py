from dataclasses import dataclass

from generated.place_sign_structure import PlaceSignStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceSign(PlaceSignStructure):
    """Sign with Place name for a PLACE.

    E.g. 'Waterloo'
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
