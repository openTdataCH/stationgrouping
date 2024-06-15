from dataclasses import dataclass, field

from generated.all_modes_enumeration import AllModesEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadVehicleMode:
    """Road Vehicle MODE: a characterisation of the operation according to the means of transport (bus, tram, coach)."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AllModesEnumeration = field(
        metadata={
            "required": True,
        }
    )
