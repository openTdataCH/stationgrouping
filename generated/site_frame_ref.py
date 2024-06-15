from dataclasses import dataclass

from generated.site_frame_ref_structure import SiteFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteFrameRef(SiteFrameRefStructure):
    """
    Reference to a SITE FRAME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
