from dataclasses import dataclass

from generated.logical_display_ref_structure import LogicalDisplayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LogicalDisplayRef(LogicalDisplayRefStructure):
    """
    Reference to a LOGICAL DISPLAY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
