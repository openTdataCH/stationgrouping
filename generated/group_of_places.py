from dataclasses import dataclass

from generated.group_of_places_version_structure import (
    GroupOfPlacesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfPlaces(GroupOfPlacesVersionStructure):
    """
    A grouping of PLACEs which will be commonly referenced for a specific purpose.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
