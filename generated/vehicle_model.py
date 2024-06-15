from dataclasses import dataclass

from generated.vehicle_model_version_structure import (
    VehicleModelVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleModel(VehicleModelVersionStructure):
    """
    A classification of public transport vehicles according to the vehicle
    scheduling requirements in MODE and capacity (e.g. standard bus, double-deck,
    ...).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
