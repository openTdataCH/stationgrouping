from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.driver_trip_time import DriverTripTime
from generated.driver_trip_time_ref import DriverTripTimeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DriverTripTimesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of DRIVER TRIP TIMEs.
    """

    class Meta:
        name = "driverTripTimes_RelStructure"

    driver_trip_time_ref_or_driver_trip_time: List[
        Union[DriverTripTimeRef, DriverTripTime]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DriverTripTimeRef",
                    "type": DriverTripTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverTripTime",
                    "type": DriverTripTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
