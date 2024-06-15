from dataclasses import dataclass, field
from typing import Optional

from generated.priceable_object_version_structure import (
    PriceableObjectVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareUnitVersionStructure(PriceableObjectVersionStructure):
    """
    Type for FARE UNIT.

    :ivar name_of_class_of_unit: Name of class associated with UNIT.
    """

    class Meta:
        name = "FareUnit_VersionStructure"

    name_of_class_of_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClassOfUnit",
            "type": "Attribute",
        },
    )
