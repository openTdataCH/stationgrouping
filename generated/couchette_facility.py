from dataclasses import dataclass, field

from generated.couchette_facility_enumeration import (
    CouchetteFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CouchetteFacility:
    """Classification of COUCHETTE FACILITY type - TPEG pti23."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: CouchetteFacilityEnumeration = field(
        default=CouchetteFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
