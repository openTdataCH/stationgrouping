from dataclasses import dataclass

from generated.fare_request_ref_structure import FareRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleTripFareRequestRefStructure(FareRequestRefStructure):
    """
    Type for Reference to a SINGLE TRIP FARE REQUEST.
    """
