from dataclasses import dataclass

from generated.geographical_structure_factor_ref_structure import (
    GeographicalStructureFactorRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalStructureFactorRef(GeographicalStructureFactorRefStructure):
    """
    Reference to a GEOGRAPHICAL STRUCTURE FACTOR.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
