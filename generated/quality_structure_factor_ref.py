from dataclasses import dataclass

from generated.quality_structure_factor_ref_structure import (
    QualityStructureFactorRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QualityStructureFactorRef(QualityStructureFactorRefStructure):
    """
    Reference to a QUALITY STRUCTURE FACTOR.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
