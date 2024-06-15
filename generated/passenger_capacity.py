from dataclasses import dataclass

from generated.passenger_capacity_structure import PassengerCapacityStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerCapacity(PassengerCapacityStructure):
    """
    Capacity for a VEHICLE TYPE and Class.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
