from dataclasses import dataclass

from generated.vehicle_entrance_ref_structure import (
    VehicleEntranceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEntranceRef(VehicleEntranceRefStructure):
    """
    Reference to an VEHICLE ENTRANCE to a SITE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
