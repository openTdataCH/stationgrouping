from dataclasses import dataclass

from generated.stop_assignment_ref_structure import StopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerStopAssignmentRefStructure(StopAssignmentRefStructure):
    """
    Type for a reference to a PASSENGER STOP ASSIGNMENT.
    """
