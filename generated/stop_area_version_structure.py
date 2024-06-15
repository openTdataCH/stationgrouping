from dataclasses import dataclass, field
from typing import Optional, Union

from generated.stop_area_ref_structure import StopAreaRefStructure
from generated.topographic_place_ref import TopographicPlaceRef
from generated.topographic_place_view import TopographicPlaceView
from generated.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopAreaVersionStructure(ZoneVersionStructure):
    """
    Type for a STOP AREA.

    :ivar public_code: Alternative public facing Code that uniquely
        identifies the STOP AREA.
    :ivar parent_stop_area_ref: Reference to any parent STOP AREA of the
        STOP AREA.
    :ivar topographic_place_ref_or_topographic_place_view:
    """

    class Meta:
        name = "StopArea_VersionStructure"

    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_stop_area_ref: Optional[StopAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentStopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    topographic_place_ref_or_topographic_place_view: Optional[
        Union[TopographicPlaceRef, TopographicPlaceView]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TopographicPlaceRef",
                    "type": TopographicPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlaceView",
                    "type": TopographicPlaceView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
