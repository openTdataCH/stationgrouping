from dataclasses import dataclass

from generated.fare_demand_factor_version_structure import (
    FareDemandFactorVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareDemandFactor(FareDemandFactorVersionStructure):
    """
    The value of a QUALITY INTERVAL or a DISTANCE MATRIX ELEMENT expressed by a
    QUALITY UNIT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
