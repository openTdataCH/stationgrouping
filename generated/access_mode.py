from dataclasses import dataclass, field

from generated.access_mode_enumeration import AccessModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessMode:
    """
    Access MODE for SITEs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccessModeEnumeration = field(
        metadata={
            "required": True,
        }
    )
