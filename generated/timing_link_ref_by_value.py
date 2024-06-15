from dataclasses import dataclass

from generated.timing_link_ref_by_value_structure import (
    TimingLinkRefByValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingLinkRefByValue(TimingLinkRefByValueStructure):
    """
    Reference to a TIMING LINK LINK BY VALUE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
