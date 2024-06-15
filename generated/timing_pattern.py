from dataclasses import dataclass

from generated.timing_pattern_version_structure import (
    TimingPatternVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPattern(TimingPatternVersionStructure):
    """
    The subset of a JOURNEY PATTERN made up only of TIMING POINTs IN JOURNEY
    PATTERN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
