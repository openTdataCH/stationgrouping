from dataclasses import dataclass

from generated.vehicle_equipment_profile_ref_structure import (
    VehicleEquipmentProfileRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEquipmentProfileRef(VehicleEquipmentProfileRefStructure):
    """
    Reference to a VEHICLE EQUIPMENT PROFILE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
