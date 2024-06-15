from dataclasses import dataclass

from generated.group_of_stop_places_structure import GroupOfStopPlacesStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfStopPlaces(GroupOfStopPlacesStructure):
    """
    Group of STOP PLACEs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
