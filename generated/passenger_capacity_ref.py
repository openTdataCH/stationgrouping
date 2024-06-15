from dataclasses import dataclass

from generated.passenger_capacity_ref_structure import (
    PassengerCapacityRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerCapacityRef(PassengerCapacityRefStructure):
    """
    Reference to a PASSENGER CAPACITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
