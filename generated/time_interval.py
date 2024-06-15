from dataclasses import dataclass

from generated.time_interval_version_structure import (
    TimeIntervalVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeInterval(TimeIntervalVersionStructure):
    """
    A factor influencing access rights definition or calculation of prices.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
