from dataclasses import dataclass

from generated.mode_ref_structure import ModeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ModeRef(ModeRefStructure):
    """
    Reference to a MODE and SUBMODE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
