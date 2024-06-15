from dataclasses import dataclass

from generated.place_version_structure import PlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Place(PlaceVersionStructure):
    """A named Place.

    A geographic place of any type which may be specified as the origin
    or destination of a trip. A PLACE may be of dimension 0 (a POINT), 1
    (a Road section) or 2 (a ZONE).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
