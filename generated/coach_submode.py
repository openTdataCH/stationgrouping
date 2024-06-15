from dataclasses import dataclass, field

from generated.coach_submode_enumeration import CoachSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CoachSubmode:
    """
    TPEG pti03 Coach submodes.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: CoachSubmodeEnumeration = field(
        default=CoachSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
