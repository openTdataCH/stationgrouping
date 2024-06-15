from dataclasses import dataclass

from generated.hail_and_ride_area_ref_structure import (
    HailAndRideAreaRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HailAndRideAreaRef(HailAndRideAreaRefStructure):
    """
    Reference to a HAIL AND RIDE AREA.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
