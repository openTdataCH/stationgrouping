from dataclasses import dataclass, field
from typing import Optional, Union

from generated.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.scheduled_stop_point_ref import ScheduledStopPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ScheduledStopPointRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of SCHEDULED STOP POINTs.
    """

    class Meta:
        name = "scheduledStopPointRefs_RelStructure"

    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref: Optional[
        Union[FareScheduledStopPointRef, ScheduledStopPointRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
