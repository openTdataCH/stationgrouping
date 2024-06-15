from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.fare_zone import FareZone
from generated.tariff_zone import TariffZone

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TariffZonesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of TARIFF ZONEs.
    """

    class Meta:
        name = "tariffZonesInFrame_RelStructure"

    fare_zone_or_tariff_zone: List[Union[FareZone, TariffZone]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareZone",
                    "type": FareZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZone",
                    "type": TariffZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
