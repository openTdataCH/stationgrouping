from dataclasses import dataclass

from generated.line_ref_structure import LineRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineRef(LineRefStructure):
    """
    Reference to a LINE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
