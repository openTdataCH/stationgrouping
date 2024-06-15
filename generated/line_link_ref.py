from dataclasses import dataclass

from generated.line_link_ref_structure import LineLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineLinkRef(LineLinkRefStructure):
    """
    Reference to a LINE LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
