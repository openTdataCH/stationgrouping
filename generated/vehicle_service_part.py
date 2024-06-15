from dataclasses import dataclass

from generated.vehicle_service_part_version_structure import (
    VehicleServicePartVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleServicePart(VehicleServicePartVersionStructure):
    """
    A part of a VEHICLE SERVICE composed of one or more BLOCKs and limited by
    periods spent at the GARAGE managing the vehicle in question.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
