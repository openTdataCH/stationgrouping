from dataclasses import dataclass, field
from typing import List

from generated.couchette_facility_enumeration import (
    CouchetteFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CouchetteFacilityList:
    """
    List of COUCHETTE FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[CouchetteFacilityEnumeration] = field(
        default_factory=lambda: [
            CouchetteFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        },
    )
