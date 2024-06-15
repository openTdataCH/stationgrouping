from dataclasses import dataclass

from generated.site_path_link_version_structure import (
    SitePathLinkVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SitePathLink(SitePathLinkVersionStructure):
    """
    A PATH LINK between two nodes that are SITE components, i.e. within a STOP
    PLACE or POINT OF INTEREST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
