from dataclasses import dataclass, field

from generated.metro_submode_enumeration import MetroSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MetroSubmode:
    """
    TPEG pti04 Metro submodes.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MetroSubmodeEnumeration = field(
        default=MetroSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
