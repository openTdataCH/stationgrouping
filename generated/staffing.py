from dataclasses import dataclass, field

from generated.staffing_enumeration import StaffingEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Staffing:
    """
    Classification of STAFFING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: StaffingEnumeration = field(
        metadata={
            "required": True,
        }
    )
