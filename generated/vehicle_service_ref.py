from dataclasses import dataclass

from generated.vehicle_service_ref_structure import VehicleServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleServiceRef(VehicleServiceRefStructure):
    """
    Reference to a VEHICLE SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
