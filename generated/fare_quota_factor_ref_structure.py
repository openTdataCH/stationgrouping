from dataclasses import dataclass

from generated.quality_structure_factor_ref_structure import (
    QualityStructureFactorRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareQuotaFactorRefStructure(QualityStructureFactorRefStructure):
    """
    Type for Reference to a FARE QUOTA FACTOR.
    """
