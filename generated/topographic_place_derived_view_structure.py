from dataclasses import dataclass, field
from typing import Optional

from generated.country_ref import CountryRef
from generated.derived_view_structure import DerivedViewStructure
from generated.multilingual_string import MultilingualString
from generated.topographic_place_ref import TopographicPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicPlaceDerivedViewStructure(DerivedViewStructure):
    """
    Type for a TOPOGRAPHIC PLACE VIEW.

    :ivar topographic_place_ref:
    :ivar name: Name of the TOPOGRAPHIC PLACE.
    :ivar short_name: Short name for TOPOGRAPHIC PLACE to be used when
        qualifying children.
    :ivar qualifier_name: Qualifying name. Place name characters only
        allowed.
    :ivar country_ref:
    """

    class Meta:
        name = "TopographicPlace_DerivedViewStructure"

    topographic_place_ref: Optional[TopographicPlaceRef] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
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
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    qualifier_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "QualifierName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
