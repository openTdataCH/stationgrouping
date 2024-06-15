from dataclasses import dataclass, field

from generated.tram_submode_enumeration import TramSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TramSubmode:
    """
    TPEG pti06 Tram submodes.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TramSubmodeEnumeration = field(
        default=TramSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
