from dataclasses import dataclass, field
from typing import Optional

from generated.derived_view_structure import DerivedViewStructure
from generated.multilingual_string import MultilingualString
from generated.stop_place_ref import StopPlaceRef
from generated.stop_type_enumeration import StopTypeEnumeration
from generated.type_of_place_refs_rel_structure import (
    TypeOfPlaceRefsRelStructure,
)
from generated.vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceDerivedViewStructure(DerivedViewStructure):
    """
    Type for STOP PLACE VIEW.

    :ivar stop_place_ref:
    :ivar name: Name of STOP PLACE.
    :ivar place_types: Classification of PLACE.
    :ivar short_name: Name of STOP PLACE.
    :ivar public_code: Short public code for passengers to use when
        uniquely identifying the stop by SMS and other self-service
        channels.
    :ivar stop_place_type: Type of STOP PLACE.
    :ivar transport_mode: Primary MODE of Vehicle transport.
    """

    class Meta:
        name = "StopPlace_DerivedViewStructure"

    stop_place_ref: Optional[StopPlaceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    place_types: Optional[TypeOfPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "placeTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_place_type: Optional[StopTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPlaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_mode: Optional[VehicleModeEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
