from dataclasses import dataclass

from generated.priceable_object_version_structure import (
    FareStructureFactorVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureFactor(FareStructureFactorVersionStructure):
    """
    A factor influencing access rights definition or calculation of prices.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
