from dataclasses import dataclass

from generated.driver_schedule_version_frame_structure import (
    DriverScheduleVersionFrameStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DriverScheduleFrame(DriverScheduleVersionFrameStructure):
    """
    A coherent set of Driver Scheduling data to which the same VALIDITY CONDITIONs
    have been assigned.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
