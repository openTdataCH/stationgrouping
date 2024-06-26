from dataclasses import dataclass

from generated.link_ref_by_value_structure import LinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineLinkRefByValueStructure(LinkRefByValueStructure):
    """
    Type for a reference to a LINE LINK BY VALUE.
    """
