from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.meeting_restriction import MeetingRestriction
from generated.overtaking_possibility import OvertakingPossibility
from generated.restricted_manoeuvre import RestrictedManoeuvre
from generated.vehicle_type_at_point import VehicleTypeAtPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkRestrictionsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of NETWORK RESTRICTION.
    """

    class Meta:
        name = "networkRestrictionsInFrame_RelStructure"

    choice: List[
        Union[
            OvertakingPossibility,
            MeetingRestriction,
            RestrictedManoeuvre,
            VehicleTypeAtPoint,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OvertakingPossibility",
                    "type": OvertakingPossibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingRestriction",
                    "type": MeetingRestriction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RestrictedManoeuvre",
                    "type": RestrictedManoeuvre,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeAtPoint",
                    "type": VehicleTypeAtPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
