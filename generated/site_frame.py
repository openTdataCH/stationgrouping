from dataclasses import dataclass

from generated.site_version_frame_structure import SiteVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteFrame(SiteVersionFrameStructure):
    """
    A coherent set of SITE data to which the same frame VALIDITY CONDITIONs have
    been assigned.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
