from dataclasses import dataclass, field

from generated.air_submode_enumeration import AirSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AirSubmode:
    """
    TPEG pti08 Air submodes.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AirSubmodeEnumeration = field(
        default=AirSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
