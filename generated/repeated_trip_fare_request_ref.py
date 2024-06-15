from dataclasses import dataclass

from generated.repeated_trip_fare_request_ref_structure import (
    RepeatedTripFareRequestRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RepeatedTripFareRequestRef(RepeatedTripFareRequestRefStructure):
    """
    Reference to a REPEATED TRIP FARE REQUEST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
