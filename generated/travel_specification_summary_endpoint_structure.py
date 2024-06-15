from dataclasses import dataclass, field
from typing import List, Optional, Union

from generated.address_ref import AddressRef
from generated.boarding_position_ref import BoardingPositionRef
from generated.postal_address_ref import PostalAddressRef
from generated.quay_ref import QuayRef
from generated.road_address_ref import RoadAddressRef
from generated.scheduled_stop_point_view import ScheduledStopPointView
from generated.tariff_zone_ref import TariffZoneRef
from generated.topographic_place_view import TopographicPlaceView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelSpecificationSummaryEndpointStructure:
    """
    Origin or destnation elements for TRAVEL SPECIFICATION Summary View.
    """

    topographic_place_view: Optional[TopographicPlaceView] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    postal_address_ref_or_road_address_ref_or_address_ref: Optional[
        Union[PostalAddressRef, RoadAddressRef, AddressRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PostalAddressRef",
                    "type": PostalAddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddressRef",
                    "type": RoadAddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AddressRef",
                    "type": AddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    scheduled_stop_point_view: Optional[ScheduledStopPointView] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quay_ref: Optional[QuayRef] = field(
        default=None,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_position_ref: Optional[BoardingPositionRef] = field(
        default=None,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tariff_zone_ref: List[TariffZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )