from dataclasses import dataclass

from generated.vehicle_type_stop_assignment_ref_structure import (
    VehicleTypeStopAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeStopAssignmentRef(VehicleTypeStopAssignmentRefStructure):
    """
    Reference to a VEHICLE TYPE STOP ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
