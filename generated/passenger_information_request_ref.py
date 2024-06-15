from dataclasses import dataclass

from generated.passenger_information_request_ref_structure import (
    PassengerInformationRequestRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerInformationRequestRef(PassengerInformationRequestRefStructure):
    """
    Reference to a PASSENGER INFORMATION REQUEST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
