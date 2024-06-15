from dataclasses import dataclass

from generated.fare_interval_version_structure import (
    FareIntervalVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareInterval(FareIntervalVersionStructure):
    """
    A factor influencing access rights definition or calculation of prices.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
