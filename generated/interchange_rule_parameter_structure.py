from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDuration

from generated.all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from generated.empty_type_2 import EmptyType2
from generated.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from generated.journey_designator import JourneyDesignator
from generated.line_in_direction_ref import LineInDirectionRef
from generated.lines_in_direction_refs_rel_structure import (
    LinesInDirectionRefsRelStructure,
)
from generated.operator_ref import OperatorRef
from generated.point_ref_structure import PointRefStructure
from generated.scheduled_stop_point_ref import ScheduledStopPointRef
from generated.scheduled_stop_point_ref_structure import (
    ScheduledStopPointRefStructure,
)
from generated.service_designator import ServiceDesignator
from generated.service_journey_ref_structure import ServiceJourneyRefStructure
from generated.stop_area_ref_structure import StopAreaRefStructure
from generated.stop_place_ref import StopPlaceRef
from generated.stop_place_ref_structure import StopPlaceRefStructure
from generated.time_demand_type_ref import TimeDemandTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleParameterStructure:
    """
    Type for INTERCHANGE RULE PARAMETER.

    :ivar transport_mode: Identifier of MODE of end Point of TRANSFER .
        Default is all modes.
    :ivar operator_ref:
    :ivar stop_area_ref: Identifier of a Place at end point of transfer.
    :ivar stop_place_ref:
    :ivar all_lines_or_lines_in_direction_refs_or_line_in_direction_ref:
    :ivar fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref:
    :ivar adjacent_stop_point_ref: Prior (feeder) or onwards
        (distributor) SCHEDULED STOP POINT before/after CONNECTION.
    :ivar adjacent_stop_place_ref: Prior (feeder) or onwards
        (distributor) SCHEDULED STOP PLACE  before/after CONNECTION.
    :ivar adjacent_point_ref: Prior (feeder) or onwards (distributor)
        POINT (not necessarily a STOP POINT) before/after connection.
    :ivar end_stop_point_ref: Identifier of end i.e. origin (feeder) or
        destination (Distributor)(SCHEDULED STOP POINT of
        feeder/distributor JOURNEY.
    :ivar time_demand_type_ref:
    :ivar
        service_journey_ref_or_journey_designator_or_service_designator:
    :ivar maximum_interchange_window: Maximum interval for making
        INTERCHANGe.
    """

    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operator_ref: Optional[OperatorRef] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_area_ref: Optional[StopAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_place_ref: Optional[StopPlaceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    all_lines_or_lines_in_direction_refs_or_line_in_direction_ref: List[
        Union[EmptyType2, LinesInDirectionRefsRelStructure, LineInDirectionRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllLines",
                    "type": EmptyType2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "linesInDirectionRefs",
                    "type": LinesInDirectionRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineInDirectionRef",
                    "type": LineInDirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
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
    adjacent_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "AdjacentStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    adjacent_stop_place_ref: Optional[StopPlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "AdjacentStopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    adjacent_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "AdjacentPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_type_ref: Optional[TimeDemandTypeRef] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_journey_ref_or_journey_designator_or_service_designator: Optional[
        Union[ServiceJourneyRefStructure, JourneyDesignator, ServiceDesignator]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyDesignator",
                    "type": JourneyDesignator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceDesignator",
                    "type": ServiceDesignator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    maximum_interchange_window: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumInterchangeWindow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
