from dataclasses import dataclass

from generated.place_sign_ref_structure import PlaceSignRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceSignRef(PlaceSignRefStructure):
    """
    Identifier of an PLACE SIGN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
