from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectServicePermissionStructure:
    """
    Type for Monitoring Service Permission.
    """

    value: float = field(
        metadata={
            "required": True,
        }
    )
