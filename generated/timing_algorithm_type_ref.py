from dataclasses import dataclass

from generated.timing_algorithm_type_ref_structure import (
    TimingAlgorithmTypeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingAlgorithmTypeRef(TimingAlgorithmTypeRefStructure):
    """
    Reference to a TIMING ALGORITHM TYPE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
