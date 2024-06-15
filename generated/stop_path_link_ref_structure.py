from dataclasses import dataclass

from generated.path_link_ref_structure import PathLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPathLinkRefStructure(PathLinkRefStructure):
    """
    Type for reference to a SITE PATH LINK.
    """
