from dataclasses import dataclass

from generated.codespace_ref_structure import CodespaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CodespaceRef(CodespaceRefStructure):
    """
    Reference to a CODESPACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
