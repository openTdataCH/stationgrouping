from dataclasses import dataclass

from generated.geographical_structure_factor_version_structure import (
    GeographicalStructureFactorVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalStructureFactor(GeographicalStructureFactorVersionStructure):
    """
    The value of a GEOGRAPHICAL INTERVAL or a DISTANCE MATRIX ELEMENT expressed by
    a GEOGRAPHICAL UNIT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
