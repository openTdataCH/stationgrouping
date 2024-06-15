from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from generated.waiting_equipment_version_structure import (
    WaitingEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ShelterEquipmentVersionStructure(WaitingEquipmentVersionStructure):
    """
    Type for a SHELTER EQUIPMENT.

    :ivar enclosed: Whether shelter is enclosed.
    :ivar distance_from_nearest_kerb: Distance from Kerb / boarding
        point.
    """

    class Meta:
        name = "ShelterEquipment_VersionStructure"

    enclosed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Enclosed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance_from_nearest_kerb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DistanceFromNearestKerb",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
