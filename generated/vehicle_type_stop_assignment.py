from dataclasses import dataclass

from generated.vehicle_type_stop_assignment_version_structure import (
    VehicleTypeStopAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeStopAssignment(VehicleTypeStopAssignmentVersionStructure):
    """
    The allocation of a stopping position of a VEHICLE TYPE for a particular
    VEHICLE JOURNEY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
