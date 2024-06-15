from dataclasses import dataclass

from generated.geographical_interval_version_structure import (
    GeographicalIntervalVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalInterval(GeographicalIntervalVersionStructure):
    """
    A factor influencing access rights definition or calculation of prices.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
