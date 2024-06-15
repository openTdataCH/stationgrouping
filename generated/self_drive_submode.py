from dataclasses import dataclass, field

from generated.self_drive_submode_enumeration import (
    SelfDriveSubmodeEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SelfDriveSubmode:
    """
    TPEG pti12 SelfDrive submodes.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: SelfDriveSubmodeEnumeration = field(
        default=SelfDriveSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
