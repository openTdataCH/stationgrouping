from dataclasses import dataclass

from generated.vehicle_version_structure import VehicleVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Vehicle(VehicleVersionStructure):
    """
    A public transport vehicle used for carrying passengers.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
