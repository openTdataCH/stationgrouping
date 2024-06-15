from dataclasses import dataclass

from generated.line_version_structure import LineVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Line(LineVersionStructure):
    """
    A group of ROUTEs which is generally known to the public by a similar name or
    number.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
