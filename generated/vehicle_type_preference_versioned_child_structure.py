from dataclasses import dataclass, field
from typing import Optional, Union

from generated.day_type_ref import DayTypeRef
from generated.fare_day_type_ref import FareDayTypeRef
from generated.journey_timing_versioned_child_structure import (
    JourneyTimingVersionedChildStructure,
)
from generated.vehicle_type_preference_ref import VehicleTypePreferenceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypePreferenceVersionedChildStructure(
    JourneyTimingVersionedChildStructure
):
    """
    Type for a VEHICLE TYPE PREFERENCE.

    :ivar rank: Relative ranking of this preference.
    :ivar fare_day_type_ref_or_day_type_ref:
    :ivar vehicle_type_preference_ref:
    """

    class Meta:
        name = "VehicleTypePreference_VersionedChildStructure"

    rank: Optional[int] = field(
        default=None,
        metadata={
            "name": "Rank",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_day_type_ref_or_day_type_ref: Optional[
        Union[FareDayTypeRef, DayTypeRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    vehicle_type_preference_ref: Optional[VehicleTypePreferenceRef] = field(
        default=None,
        metadata={
            "name": "VehicleTypePreferenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
