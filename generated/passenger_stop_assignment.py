from dataclasses import dataclass

from generated.passenger_stop_assignment_version_structure import (
    PassengerStopAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerStopAssignment(PassengerStopAssignmentVersionStructure):
    """
    Assignment of a SCHEDULED STOP POINT to a STOP PLACE and QUAY, etc.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
