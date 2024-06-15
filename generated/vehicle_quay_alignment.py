from dataclasses import dataclass

from generated.vehicle_quay_alignment_version_structure import (
    VehicleQuayAlignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleQuayAlignment(VehicleQuayAlignmentVersionStructure):
    """
    Designated Position within a VEHICLE STOPPING PLACE for a Vehicle to stop.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
