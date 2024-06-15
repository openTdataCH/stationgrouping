from dataclasses import dataclass

from generated.fare_frame_version_frame_structure import (
    FareFrameVersionFrameStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareFrame(FareFrameVersionFrameStructure):
    """
    A coherent set of Vehicle Scheduling data to which the same VALIDITY CONDITIONs
    have been assigned.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
