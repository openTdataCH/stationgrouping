from dataclasses import dataclass, field

from generated.limitation_status_enumeration import LimitationStatusEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WheelchairAccess:
    """
    Whether a PLACE is wheelchair accessible.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: LimitationStatusEnumeration = field(
        default=LimitationStatusEnumeration.FALSE,
        metadata={
            "required": True,
        },
    )
