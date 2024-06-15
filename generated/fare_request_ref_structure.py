from dataclasses import dataclass

from generated.passenger_information_request_ref_structure import (
    PassengerInformationRequestRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareRequestRefStructure(PassengerInformationRequestRefStructure):
    """
    Type for Reference to a FARE REQUEST.
    """
