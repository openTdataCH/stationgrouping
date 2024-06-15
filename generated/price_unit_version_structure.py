from dataclasses import dataclass, field
from typing import Optional

from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceUnitVersionStructure(TypeOfValueVersionStructure):
    """
    Type for PRICE UNIT.

    :ivar precision: Precision to use for units.
    """

    class Meta:
        name = "PriceUnit_VersionStructure"

    precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "Precision",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
