from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from generated.site_equipment_version_structure import (
    SiteEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WaitingEquipmentVersionStructure(SiteEquipmentVersionStructure):
    """
    Type for Waiting EQUIPMENT.

    :ivar seats: Number of seats in Area.
    :ivar width: Width of area.
    :ivar length: Length of Area.
    :ivar step_free: Whether area is step free.
    :ivar wheelchair_area_width: Width of Wheelchair Area.
    :ivar wheelchair_area_length: Width of Wheelchair Area.
    :ivar smoking_allowed: Whether smoking is allowed in area.
    :ivar heated: Whether shelter has heating.
    :ivar air_conditioned: Whether shelter has air conditioining.
    """

    class Meta:
        name = "WaitingEquipment_VersionStructure"

    seats: Optional[int] = field(
        default=None,
        metadata={
            "name": "Seats",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    step_free: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StepFree",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_area_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WheelchairAreaWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_area_length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WheelchairAreaLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    smoking_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmokingAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    heated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Heated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    air_conditioned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AirConditioned",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
