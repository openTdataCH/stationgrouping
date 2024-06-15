from dataclasses import dataclass

from generated.group_of_places_ref_structure import GroupOfPlacesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfPlacesRef(GroupOfPlacesRefStructure):
    """
    Reference to a GROUP OF PLACEs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
