from dataclasses import dataclass, field

from generated.all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllVehicleModes:
    """
    All MODEs including vehicle transport and self drive.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AllVehicleModesOfTransportEnumeration = field(
        metadata={
            "required": True,
        }
    )
