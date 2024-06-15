from dataclasses import dataclass

from generated.driver_trip_time_ref_structure import DriverTripTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DriverTripTimeRef(DriverTripTimeRefStructure):
    """
    Reference to a DRIVER TRIP TIME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
