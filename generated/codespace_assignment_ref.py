from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CodespaceAssignmentRef:
    """
    Reference to a CODESPACE ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
