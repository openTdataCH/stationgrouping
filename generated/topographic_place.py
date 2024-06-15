from dataclasses import dataclass

from generated.topographic_place_version_structure import (
    TopographicPlaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicPlace(TopographicPlaceVersionStructure):
    """A town, city, village, suburb, quarter or other name settlement within a
    country.

    Provides a Gazetteer of Transport related place names.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
