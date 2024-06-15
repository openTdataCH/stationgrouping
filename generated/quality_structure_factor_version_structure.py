from dataclasses import dataclass, field
from typing import Optional

from generated.priceable_object_version_structure import (
    FareStructureFactorVersionStructure,
)
from generated.quality_structure_factor_prices_rel_structure import (
    QualityStructureFactorPricesRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QualityStructureFactorVersionStructure(
    FareStructureFactorVersionStructure
):
    """
    Type for QUALITY STRUCTURE FACTOR.

    :ivar value: Value associated with QUALITY STRUCTURE FACTOR.
    :ivar prices: PRICEs for QUALITY STRUCTURE FACTOR.
    """

    class Meta:
        name = "QualityStructureFactor_VersionStructure"

    value: Optional[object] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional[QualityStructureFactorPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
