from dataclasses import dataclass

from generated.vehicle_equipment_profile_version_structure import (
    VehicleEquipmentProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEquipmentProfile(VehicleEquipmentProfileVersionStructure):
    """Each instantiation of this ENTITY gives the number of items of one TYPE OF
    EQUIPMENT a VEHICLE MODEL should contain for a given PURPOSE OF EQUIPMENT
    PROFILE.

    The set of instantiations for one VEHICLE MODEL and one purpose
    gives one complete 'profile'.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
