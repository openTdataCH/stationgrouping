from dataclasses import dataclass

from generated.link_sequence_ref_structure import LinkSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPatternRefStructure(LinkSequenceRefStructure):
    """
    Type for a reference to a TIMING PATTERN.
    """
