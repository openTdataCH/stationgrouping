from dataclasses import dataclass, field
from typing import Optional

from generated.country_ref import CountryRef
from generated.group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from generated.place_ref_structure import PlaceRefStructure
from generated.place_refs_rel_structure import PlaceRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfPlacesVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for GROUP OF PLACES.

    :ivar members: PLACEs in GROUP OF PLACEs.
    :ivar country_ref:
    :ivar main_place_ref: Primary PLACE in GROUP OF PLACEs, if relevant.
    """

    class Meta:
        name = "GroupOfPlaces_VersionStructure"

    members: Optional[PlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    main_place_ref: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "MainPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
