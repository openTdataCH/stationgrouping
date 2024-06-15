from dataclasses import dataclass

from generated.vehicle_ref_structure import VehicleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleRef(VehicleRefStructure):
    """
    Reference to a VEHICLE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
