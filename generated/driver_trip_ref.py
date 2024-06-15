from dataclasses import dataclass

from generated.driver_trip_ref_structure import DriverTripRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DriverTripRef(DriverTripRefStructure):
    """
    Reference to a DRIVER TRIP.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
