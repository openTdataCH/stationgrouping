from dataclasses import dataclass

from generated.timing_link_version_structure import TimingLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingLink(TimingLinkVersionStructure):
    """An ordered pair of TIMING POINTs for which run times may be recorded.

    Timing links are directional - there will be separate links for each direction of a route.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
