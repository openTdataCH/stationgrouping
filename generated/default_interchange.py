from dataclasses import dataclass

from generated.default_interchange_version_structure import (
    DefaultInterchangeVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultInterchange(DefaultInterchangeVersionStructure):
    """A quality parameter fixing the acceptable duration (standard and maximum)
    for an INTERCHANGE to be planned between two SCHEDULED STOP POINTs.

    This parameter will be used to control whether any two VEHICLE
    JOURNEYs serving those points may be in connection.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
