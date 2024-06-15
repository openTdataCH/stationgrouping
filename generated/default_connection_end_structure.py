from dataclasses import dataclass, field
from typing import Optional

from generated.operator_view import OperatorView
from generated.vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultConnectionEndStructure:
    """
    Type for a DEFAULT TRANSFER.

    :ivar transport_mode: Identifier of MODE of end point of TRANSFER.
    :ivar operator_view:
    """

    transport_mode: Optional[VehicleModeEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operator_view: Optional[OperatorView] = field(
        default=None,
        metadata={
            "name": "OperatorView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
