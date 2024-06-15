from dataclasses import dataclass, field
from typing import List, Optional, Union

from generated.alternative_names_rel_structure import (
    AlternativeNamesRelStructure,
)
from generated.flexible_area import FlexibleArea
from generated.flexible_area_ref import FlexibleAreaRef
from generated.hail_and_ride_area import HailAndRideArea
from generated.hail_and_ride_area_ref import HailAndRideAreaRef
from generated.line_refs_rel_structure import LineRefsRelStructure
from generated.multilingual_string import MultilingualString
from generated.place_version_structure import PlaceVersionStructure
from generated.vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleStopPlaceVersionStructure(PlaceVersionStructure):
    """
    Type for a FLEXIBLE STOP PLACE.

    :ivar name_suffix: Further suffix to name that may be used in some
        contexts.
    :ivar alternative_names: Alternative names.
    :ivar transport_mode: Primary MODE of Vehicle transport.
    :ivar public_code: Short public code for passengers to use when
        uniquely identifying the stop by SMS and other self-service
        channels.
    :ivar areas: Areas in FLEXIBLE STOP PLACE.
    :ivar lines: Lines  for  FLEXIBLE STOP PLACE.
    """

    class Meta:
        name = "FlexibleStopPlace_VersionStructure"

    name_suffix: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
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
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    areas: Optional["FlexibleStopPlaceVersionStructure.Areas"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lines: Optional[LineRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class Areas:
        choice: List[
            Union[
                FlexibleArea,
                FlexibleAreaRef,
                HailAndRideArea,
                HailAndRideAreaRef,
            ]
        ] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "FlexibleArea",
                        "type": FlexibleArea,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "FlexibleAreaRef",
                        "type": FlexibleAreaRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "HailAndRideArea",
                        "type": HailAndRideArea,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "HailAndRideAreaRef",
                        "type": HailAndRideAreaRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
