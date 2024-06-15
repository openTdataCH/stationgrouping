from dataclasses import dataclass, field
from typing import Optional

from generated.fare_unit_version_structure import FareUnitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareUnit(FareUnitVersionStructure):
    """
    A factor influencing access rights definition or calculation of prices.

    :ivar name_of_class: Name of Class of the ENTITY. Allows reflection.
        Fixed for each ENTITY type.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_of_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        },
    )
