from dataclasses import dataclass, field
from typing import Optional, Union

from generated.dead_run_endpoint_structure import DeadRunEndpointStructure
from generated.dead_run_type_enumeration import DeadRunTypeEnumeration
from generated.direction_type import DirectionType
from generated.flexible_line_ref import FlexibleLineRef
from generated.group_of_services_refs_rel_structure import (
    GroupOfServicesRefsRelStructure,
)
from generated.line_ref import LineRef
from generated.operator_ref import OperatorRef
from generated.train_number_refs_rel_structure import (
    TrainNumberRefsRelStructure,
)
from generated.vehicle_journey_version_structure import (
    VehicleJourneyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeadRunVersionStructure(VehicleJourneyVersionStructure):
    """
    Type for DEAD RUN.

    :ivar operator_ref:
    :ivar flexible_line_ref_or_line_ref:
    :ivar direction_type:
    :ivar groups_of_services: GROUPS OF SERVICEs to which a DEAD RUN
        belongs.
    :ivar train_numbers: TRAIN NUMBERs -= derived through JOURNEY PARTs
        of a JOURNEY - for a multi-part JOURNEY only.
    :ivar origin: Origin  for DEAD RUN. Can be Derived from JORUNEY
        PATTERN.
    :ivar destination: Destination  for DEAD RUN. Can be derived from
        JORUNEY PATTERN.
    :ivar dead_run_type: Type of DEAD RUN.
    """

    class Meta:
        name = "DeadRun_VersionStructure"

    operator_ref: Optional[OperatorRef] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_line_ref_or_line_ref: Optional[
        Union[FlexibleLineRef, LineRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    direction_type: Optional[DirectionType] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_services: Optional[GroupOfServicesRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_numbers: Optional[TrainNumberRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "trainNumbers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    origin: Optional[DeadRunEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination: Optional[DeadRunEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dead_run_type: Optional[DeadRunTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DeadRunType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
