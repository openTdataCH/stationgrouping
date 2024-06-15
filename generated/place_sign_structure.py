from dataclasses import dataclass, field
from typing import Optional

from generated.multilingual_string import MultilingualString
from generated.place_ref import PlaceRef
from generated.sign_equipment_version_structure import (
    SignEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceSignStructure(SignEquipmentVersionStructure):
    """
    Type for a PLACE SIGN.

    :ivar place_name: Name of Stop.
    :ivar place_ref:
    """

    place_name: MultilingualString = field(
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    place_ref: Optional[PlaceRef] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
