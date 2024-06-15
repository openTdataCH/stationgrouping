from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlTime

from generated.day_type_ref import DayTypeRef
from generated.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from generated.derived_view_structure import DerivedViewStructure
from generated.destination_display_view import DestinationDisplayView
from generated.fare_day_type_ref import FareDayTypeRef
from generated.frequency_structure import FrequencyStructure
from generated.journey_pattern_ref import JourneyPatternRef
from generated.multilingual_string import MultilingualString
from generated.service_journey_pattern_ref import ServiceJourneyPatternRef
from generated.service_journey_ref_structure import ServiceJourneyRefStructure
from generated.service_pattern_ref import ServicePatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ConnectingJourneyDerivedViewStructure(DerivedViewStructure):
    """
    Type for CONNECTING JOURNEY VIEW.

    :ivar service_journey_ref: Service Journey to which srevice
        connects.
    :ivar departure_time_or_frequency:
    :ivar name: Name of journey.
    :ivar destination_display_view:
    :ivar fare_day_type_ref_or_day_type_ref:
    :ivar choice:
    :ivar connecting_order: Order of Point within Connecting journey as
        an absolute number.
    :ivar connecting_visit_number: Order of Point within Connecting as
        number of visits to the same stop.  Default is 1.
    """

    class Meta:
        name = "ConnectingJourney_DerivedViewStructure"

    service_journey_ref: ServiceJourneyRefStructure = field(
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    departure_time_or_frequency: Optional[
        Union[XmlTime, FrequencyStructure]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DepartureTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Frequency",
                    "type": FrequencyStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_display_view: Optional[DestinationDisplayView] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayView",
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
    choice: Optional[
        Union[
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    connecting_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "ConnectingOrder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    connecting_visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "ConnectingVisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
