from dataclasses import dataclass

from generated.timing_link_ref_structure import TimingLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingLinkRef(TimingLinkRefStructure):
    """
    Reference to a TIMING LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
