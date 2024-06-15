from dataclasses import dataclass, field
from typing import Optional, Union

from generated.derived_view_structure import DerivedViewStructure
from generated.multilingual_string import MultilingualString
from generated.scheduled_stop_point_ref_structure import (
    ScheduledStopPointRefStructure,
)
from generated.tariff_zone_ref_structure import TariffZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementDerivedViewStructure(DerivedViewStructure):
    """
    Type for CONNECTING JOURNEY VIEW.

    :ivar start_stop_point_ref_or_start_tariff_zone_ref:
    :ivar start_name: Name of Start Stop Point.
    :ivar end_stop_point_ref_or_end_tariff_zone_ref:
    :ivar end_name: Name of Stop Point.
    """

    class Meta:
        name = "DistanceMatrixElement_DerivedViewStructure"

    start_stop_point_ref_or_start_tariff_zone_ref: Optional[
        Union[ScheduledStopPointRefStructure, TariffZoneRefStructure]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StartStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartTariffZoneRef",
                    "type": TariffZoneRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    start_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "StartName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_stop_point_ref_or_end_tariff_zone_ref: Optional[
        Union[ScheduledStopPointRefStructure, TariffZoneRefStructure]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EndStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndTariffZoneRef",
                    "type": TariffZoneRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    end_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "EndName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
