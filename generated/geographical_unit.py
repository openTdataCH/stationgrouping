from dataclasses import dataclass

from generated.geographical_unit_version_structure import (
    GeographicalUnitVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalUnit(GeographicalUnitVersionStructure):
    """
    A factor influencing access rights definition or calculation of prices.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
