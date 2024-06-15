from dataclasses import dataclass

from generated.driver_trip_time_version_structure import (
    DriverTripTimeVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DriverTripTime(DriverTripTimeVersionStructure):
    """
    A part of a BLOCK composed of consecutive VEHICLE JOURNEYs defined for the same
    DAY TYPE, all operated on the same LINE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
