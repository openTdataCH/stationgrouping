from dataclasses import dataclass

from generated.vehicle_position_alignment_version_structure import (
    VehiclePositionAlignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePositionAlignment(VehiclePositionAlignmentVersionStructure):
    """
    Designated Position within a VEHICLE STOPPING PLACE for a Vehicle to stop.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
