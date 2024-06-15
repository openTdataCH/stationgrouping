from dataclasses import dataclass

from generated.quality_structure_factor_price_ref_structure import (
    QualityStructureFactorPriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QualityStructureFactorPriceRef(QualityStructureFactorPriceRefStructure):
    """
    Reference to a QUALITY STRUCTURE FACTOR PRICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
