from dataclasses import dataclass, field

from generated.accommodation_access_enumeration import (
    AccommodationAccessEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccommodationAccess:
    """
    Classification of ACCOMMODATION ACCESS type -
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccommodationAccessEnumeration = field(
        metadata={
            "required": True,
        }
    )
