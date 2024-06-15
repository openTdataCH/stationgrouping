from dataclasses import dataclass, field
from typing import Optional

from generated.derived_view_structure import DerivedViewStructure
from generated.direction_ref import DirectionRef
from generated.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DirectionDerivedViewStructure(DerivedViewStructure):
    """
    Type for DIRECTION VIEW.

    :ivar direction_ref:
    :ivar name: Name of DIRECTION.
    """

    class Meta:
        name = "Direction_DerivedViewStructure"

    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
