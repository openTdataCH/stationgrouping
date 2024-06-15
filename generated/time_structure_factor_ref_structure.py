from dataclasses import dataclass

from generated.fare_structure_factor_ref_structure import (
    FareStructureFactorRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeStructureFactorRefStructure(FareStructureFactorRefStructure):
    """
    Type for Reference to a TIME STRUCTURE FACTOR.
    """
