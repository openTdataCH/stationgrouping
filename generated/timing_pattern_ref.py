from dataclasses import dataclass

from generated.timing_pattern_ref_structure import TimingPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPatternRef(TimingPatternRefStructure):
    """
    Reference to a TIMING PATTERN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
