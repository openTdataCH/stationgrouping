from dataclasses import dataclass, field
from typing import Optional, Union

from generated.all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from generated.derived_view_structure import DerivedViewStructure
from generated.flexible_line_ref import FlexibleLineRef
from generated.line_ref import LineRef
from generated.multilingual_string import MultilingualString
from generated.operator_ref import OperatorRef
from generated.transport_submode import TransportSubmode
from generated.type_of_line_ref import TypeOfLineRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineDerivedViewStructure(DerivedViewStructure):
    """
    Type for a LINE VIEW.

    :ivar flexible_line_ref_or_line_ref:
    :ivar public_code: Identifier of LINE.
    :ivar name: Name of LINE.
    :ivar short_name: Short name of LINE.
    :ivar transport_mode: TRANSPORT MODE of LINE.
    :ivar transport_submode:
    :ivar operator_ref:
    :ivar type_of_line_ref:
    """

    class Meta:
        name = "Line_DerivedViewStructure"

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
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
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
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_submode: Optional[TransportSubmode] = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
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
    type_of_line_ref: Optional[TypeOfLineRef] = field(
        default=None,
        metadata={
            "name": "TypeOfLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
