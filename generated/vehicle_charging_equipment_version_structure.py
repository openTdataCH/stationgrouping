from dataclasses import dataclass, field
from typing import Optional

from generated.place_equipment_version_structure import (
    PlaceEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleChargingEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    """
    Type for a VEHICLE CHARGING EQUIPMENT.

    :ivar free_recharging: whether shelter is enclosed.
    :ivar reservation_required: Whether reservation is required.
    :ivar reservation_url: Type of storage.
    """

    class Meta:
        name = "VehicleChargingEquipment_VersionStructure"

    free_recharging: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FreeRecharging",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reservation_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReservationRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reservation_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
