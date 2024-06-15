from dataclasses import dataclass

from generated.site_connection_ref_structure import SiteConnectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteConnectionRef(SiteConnectionRefStructure):
    """
    Reference to a SITE CONNECTION link.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
