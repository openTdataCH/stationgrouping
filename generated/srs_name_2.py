from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SrsName2:
    """
    Name of GML Spatial coordinate Reference system.
    """

    class Meta:
        name = "SrsName"
        namespace = "http://www.netex.org.uk/netex"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
