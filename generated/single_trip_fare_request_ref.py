from dataclasses import dataclass

from generated.single_trip_fare_request_ref_structure import (
    SingleTripFareRequestRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleTripFareRequestRef(SingleTripFareRequestRefStructure):
    """
    Reference to a SINGLE TRIP FARE REQUEST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
