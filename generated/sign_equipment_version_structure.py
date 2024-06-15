from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from generated.audio_trigger_method_enumeration import (
    AudioTriggerMethodEnumeration,
)
from generated.installed_equipment_version_structure import (
    InstalledEquipmentVersionStructure,
)
from generated.multilingual_string import MultilingualString
from generated.print_presentation_structure import PrintPresentationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SignEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    """
    Type for SIGN EQUIPMENT.

    :ivar height: Height of SIGN in metres.
    :ivar width: Width of sign in metres.
    :ivar height_from_floor: Height of bottom edge of sign from floor in
        metres.
    :ivar placement: Description of location of sign.
    :ivar brand_graphic: Graphic for sign.
    :ivar sign_graphic: Graphic or sign.
    :ivar machine_readable: Whether SIGN is machine readable.
    :ivar as_braille: Whether SIGN is readable in Braille. +v1.1
    :ivar audio_trigger_method: How the display may be read by the audio
        tool. +v1.1
    :ivar printed_presentation: Presentatuon characteristics including
        font size +v1.1 .
    :ivar contrast: Luminance gap between text and background. A ratio
        of at least 3 is expected. +v1.1
    """

    class Meta:
        name = "SignEquipment_VersionStructure"

    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_from_floor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightFromFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    placement: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Placement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    brand_graphic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandGraphic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sign_graphic: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignGraphic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    machine_readable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MachineReadable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    as_braille: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AsBraille",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_trigger_method: Optional[AudioTriggerMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "AudioTriggerMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    printed_presentation: Optional[PrintPresentationStructure] = field(
        default=None,
        metadata={
            "name": "PrintedPresentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contrast: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Contrast",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
