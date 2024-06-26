from dataclasses import dataclass, field
from typing import List

from generated.emergency_service_enumeration import EmergencyServiceEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EmergencyServiceList:
    """
    List of EMERGENCY SERVICE FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[EmergencyServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
