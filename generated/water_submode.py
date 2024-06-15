from dataclasses import dataclass, field

from generated.water_submode_enumeration import WaterSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WaterSubmode:
    """
    TPEG pti07 Water submodes.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: WaterSubmodeEnumeration = field(
        default=WaterSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
