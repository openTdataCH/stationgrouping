from dataclasses import dataclass

from generated.installed_equipment_ref_structure import (
    InstalledEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEquipmentRef(InstalledEquipmentRefStructure):
    """
    Reference to a WHEELCHAIR VEHICLE EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
