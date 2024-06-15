from dataclasses import dataclass

from generated.time_demand_profile_version_structure import (
    TimeDemandProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeDemandProfile(TimeDemandProfileVersionStructure):
    """
    TIME DEMAND PROFILE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
