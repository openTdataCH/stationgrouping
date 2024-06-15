from dataclasses import dataclass

from generated.quality_structure_factor_price_versioned_child_structure import (
    QualityStructureFactorPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QualityStructureFactorPrice(
    QualityStructureFactorPriceVersionedChildStructure
):
    """A set of all possible price features of a QUALITY STRUCTURE FACTOR: default total price etc."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
