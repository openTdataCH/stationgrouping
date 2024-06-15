from dataclasses import dataclass

from generated.vehicle_model_ref_structure import VehicleModelRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleModelRef(VehicleModelRefStructure):
    """
    Reference to a VEHICLE MODEL.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
