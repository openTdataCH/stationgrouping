from dataclasses import dataclass

from generated.passenger_seat_ref_structure import PassengerSeatRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerSeatRef(PassengerSeatRefStructure):
    """
    Reference to a  PASSENGER SEAT +v1.1.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
