from dataclasses import dataclass, field
from typing import Optional

from generated.delivery_variant_type_enumeration import (
    DeliveryVariantTypeEnumeration,
)
from generated.destination_display_context_enumeration import (
    DestinationDisplayContextEnumeration,
)
from generated.destination_display_ref import DestinationDisplayRef
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.multilingual_string import MultilingualString
from generated.vias_rel_structure import ViasRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DestinationDisplayVariantVersionStructure(DataManagedObjectStructure):
    """
    Type for DESTINATION DISPLAY VARIANT.

    :ivar destination_display_ref:
    :ivar destination_display_context: Context in which to use the
        secondary name.  Default is 'any'+v1.1
    :ivar destination_display_variant_media_type: Type of DESTINATION
        DISPLAY VARIANT. Default is 'any'.
    :ivar name: Name of destination on DESTINATION DISPLAY.
    :ivar short_name: Short Name on DESTINATION DISPLAY.
    :ivar side_text: Name of destination to show on side of VEHICLE.
    :ivar front_text: Name of destination to show on front of VEHICLE.
    :ivar driver_display_text: Text to show to Driver or Staff for the
        DESTINATION DISPLAY.
    :ivar vias: Destinations that the Service goes via.
    """

    class Meta:
        name = "DestinationDisplayVariant_VersionStructure"

    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_display_context: Optional[
        DestinationDisplayContextEnumeration
    ] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_display_variant_media_type: DeliveryVariantTypeEnumeration = (
        field(
            default=DeliveryVariantTypeEnumeration.ANY,
            metadata={
                "name": "DestinationDisplayVariantMediaType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            },
        )
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
    side_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "SideText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    front_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "FrontText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    driver_display_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "DriverDisplayText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vias: Optional[ViasRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
