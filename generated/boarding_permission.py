from dataclasses import dataclass, field

from generated.boarding_permission_enumeration import (
    BoardingPermissionEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BoardingPermission:
    """Classification of BOARDING PERMISSION - UIC 7161 Code list."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: BoardingPermissionEnumeration = field(
        metadata={
            "required": True,
        }
    )
