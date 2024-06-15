from dataclasses import dataclass

from generated.passenger_stop_assignment_ref_structure import (
    PassengerStopAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerStopAssignmentRef(PassengerStopAssignmentRefStructure):
    """
    Reference to a PASSENGER STOP ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
