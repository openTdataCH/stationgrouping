from dataclasses import dataclass

from generated.stop_place_version_structure import StopPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlace(StopPlaceVersionStructure):
    """Version of a named place where public transport may be accessed.

    May be a building complex (e.g. a station) or an on-street location.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
