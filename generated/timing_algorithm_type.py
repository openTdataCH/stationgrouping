from dataclasses import dataclass

from generated.timing_algorithm_type_value_structure import (
    TimingAlgorithmTypeValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingAlgorithmType(TimingAlgorithmTypeValueStructure):
    """
    Classification of a TIMING ALGORITHM.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
