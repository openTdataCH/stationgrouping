from dataclasses import dataclass

from generated.passenger_stop_assignment_derived_view_structure import (
    PassengerStopAssignmentDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QuayAssignmentView(PassengerStopAssignmentDerivedViewStructure):
    """
    Assignment to a specific QUAY within the STOP PLACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
