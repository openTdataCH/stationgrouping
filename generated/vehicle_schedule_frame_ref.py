from dataclasses import dataclass

from generated.vehicle_schedule_frame_ref_structure import (
    VehicleScheduleFrameRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleScheduleFrameRef(VehicleScheduleFrameRefStructure):
    """
    Reference to a VEHICLE SCHEDULE FRAME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
